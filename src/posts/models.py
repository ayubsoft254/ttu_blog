from django.db import models

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
