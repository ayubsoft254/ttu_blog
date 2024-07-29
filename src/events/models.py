from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="events")
    category = models.ForeignKey('EventCategory', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.title   

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_event')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="events", blank=True)

    def __str__(self):
        return self.user.username

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='event_comments')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.content_object}"

class Rating(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_ratings')
    score = models.IntegerField()

    def __str__(self):
        return f"Rating by {self.user} on {self.content_object}"

class Bookmark(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_bookmarks')

    def __str__(self):
        return f"Bookmark by {self.user} on {self.content_object}"

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True) 
    status = models.CharField(max_length=100)

    def clean(self):
        if not self.user and (not self.name or not self.email):
            raise ValidationError('Either a registered user or name and email of an unregistered user must be provided.')

    def __str__(self):
<<<<<<< HEAD
        return f"Attendance for {self.event} by {'registered user' if self.user else self.name}"
=======
        return f"Attendance for {self.event} by {'registered user' if self.user else self.name}"
>>>>>>> d6968ac80f4093cd0fe50aaed5f9555c6bed6db8
