from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    
    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    text = models.TextField()
    dated = models.DateField(default=timezone.now())
    image = models.ImageField(upload_to='uploads/', default='uploads/default.jpg')
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)