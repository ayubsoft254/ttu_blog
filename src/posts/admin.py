from django.contrib import admin
from .models import Story, Comment, Opinion, Like

# Register your models here.

admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Opinion)
admin.site.register(Like)
