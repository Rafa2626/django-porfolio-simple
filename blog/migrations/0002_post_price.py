# Generated by Django 5.0.1 on 2024-01-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="price",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
