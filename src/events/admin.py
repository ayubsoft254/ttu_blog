from django.contrib import admin
from .models import Event, UserProfile, EventCategory, Ticket, Comment, Rating, Bookmark, Attendance

# Register your models here.
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(EventCategory)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Bookmark)
admin.site.register(Attendance)
