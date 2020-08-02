from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'user', 'id']


admin.site.register(Post, PostAdmin)
