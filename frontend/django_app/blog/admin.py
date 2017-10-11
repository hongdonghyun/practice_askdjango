from django.contrib import admin

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_date')


@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    list_display = ('post', 'message', 'created_date')
