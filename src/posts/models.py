from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name      
class Story(models.Model):
    img_title = models.ImageField(upload_to='media/images')
    title = models.CharField(max_length=100)
    snip = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    

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
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_comments')
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.story}"   


    

class Like(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user} on {self.story}"
    
    

class Report(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user} on {self.story}"