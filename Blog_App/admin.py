from django.contrib import admin

# Register your models here.
from Blog_App.models import Blog_User,Post_Blog,Comment

@admin.register(Post_Blog)
class blog(admin.ModelAdmin):
    list_display = ['title','author','created_date','blog_like']
    list_filter = ['author','created_date']

@admin.register(Blog_User)
class blog_user(admin.ModelAdmin):
    list_display = ['user_name','user_password']

@admin.register(Comment)
class comment(admin.ModelAdmin):
    list_display = ['blog_title','name','comment']
    list_filter = ['blog_title','name']