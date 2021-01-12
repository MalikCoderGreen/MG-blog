from django.contrib import admin
from ps_blog_app.models import category, blog_post, comment, UserProfileInfo

# Register your models here.
admin.site.register(category)
admin.site.register(blog_post)
admin.site.register(UserProfileInfo)
