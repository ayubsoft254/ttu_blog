from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)  # Assuming there's an author field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
class Opinion(models.Model):
    img_title = models.ImageField(upload_to='media/images')
    title = models.CharField(max_length=100)
    snip = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
    
    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    
        