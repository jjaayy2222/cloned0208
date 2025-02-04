# Generated by Django 5.1.5 on 2025-02-04 03:04

from django.db import migrations

def set_default_user(apps, schema_editor):
    Post = apps.get_model('app', 'Post')
    User = apps.get_model('auth', 'User')

    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        admin_user = User.objects.first()

    if admin_user:
        Post.objects.filter(user__isnull=True).update(user=admin_user)

class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_aigeneration_delete_article_post_user"),
    ]

    operations = [
        migrations.RunPython(set_default_user)
    ]
