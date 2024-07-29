from django.contrib import admin

from .models import Story, Opinion
from .models import  Story, Comment, Opinion, Like

# Register your models here.

from .models import Story, Comment, Opinion, Like
admin.site.register(Story)
admin.site.register(Opinion)
admin.site.register(Like)
