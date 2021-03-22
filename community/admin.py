from django.contrib import admin


from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'heading',
        'body',
        'image',
        'user_profile',
    )

    ordering = ('heading',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'user_profile',
    )

    ordering = ('user_profile',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
