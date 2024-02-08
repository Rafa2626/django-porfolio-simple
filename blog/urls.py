from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.render_posts, name='posts'),
    path('<int:post_id>/', views.post_detail, name="post_detail"),  
    path('add_post/', views.add_post, name='add_post'), 
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/confirm_delete/<int:post_id>/', views.confirm_delete_post, name='confirm_delete_post'),
]
