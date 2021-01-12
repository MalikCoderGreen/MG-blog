from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model will inherit from Django 'User' model.
class UserProfileInfo(models.Model): 
    #user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    posts = models.ManyToManyField('blog_post', related_name='b_posts')

    def __str__(self): 
        return self.user.username

# All blog posts must have a category. 
class category(models.Model): 
    name = models.CharField(max_length=30)
    def __str__(self): 
        return self.name

# Blog posts that can be created if a user is logged in.
class blog_post(models.Model): 
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('category', related_name='posts')
    
    def __str__(self): 
        return self.title
# Model for comments on a blog post.
class comment(models.Model): 
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog_post', on_delete=models.CASCADE)


