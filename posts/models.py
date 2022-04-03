from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#!Post Model
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    title = models.CharField(max_length=100)
    body = models.TextField()
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)

    @property 
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

#!Like Model
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(max_length=100,choices=LIKE_CHOICES,default='Like')
    
    def __str__(self):
        return str(self.post)
    