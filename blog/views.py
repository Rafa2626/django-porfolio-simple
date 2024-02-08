from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.admin.views.decorators import staff_member_required


def render_posts(request):
    posts = Post.objects.all
    return render(request,  'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post": post})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')  
    else:
        form = PostForm()
    return render(request, "add_post.html", {'form': form})


@login_required
@staff_member_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


@login_required
@staff_member_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        return redirect('blog:confirm_delete_post', post_id=post_id)
    return render(request, 'blog/delete_post.html', {'post': post})

@login_required
@staff_member_required
def confirm_delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:posts')
    return render(request, 'confirm_delete.html', {'post': post})
