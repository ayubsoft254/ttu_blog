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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.title   

