from django.contrib import admin
from .models import Story, Opinion
from .models import Category, Tag, Story, Comment, Opinion, Like

# Register your models here.
admin.site.register(Story)
admin.site.register(Opinion)
admin.site.register(Like)
