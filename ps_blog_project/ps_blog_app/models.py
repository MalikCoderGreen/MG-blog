from django.db import models

# Create your models here.
class category(models.Model): 
    name = models.CharField(max_length=30)

class blog_post(models.Model): 
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('category', related_name='posts')
    
    def __str__(self): 
        return self.title

class comment(models.Model): 
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog_post', on_delete=models.CASCADE)

    