from django.db import models
from apps.users.models import User

# Create your models here.
class Post(models.Model):
    photo = models.ImageField(blank=True)
    title = models.CharField(max_length=24)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    content = models.TextField(max_length=200)
    created_date = models.DateField(auto_now_add = True)
    like = models.IntegerField(default=0)
    is_liked = models.BooleanField(default=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=100)
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
