from django.contrib import admin
from core.models import Profile, Comment_Comment, Comment_Likes, Post, Post_Likes, Post_Comment, Follows

# Register your models here.


class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Profile)
admin.site.register(Comment_Comment)
admin.site.register(Comment_Likes)
admin.site.register(Post)
admin.site.register(Post_Likes)
admin.site.register(Post_Comment)
admin.site.register(Follows)
