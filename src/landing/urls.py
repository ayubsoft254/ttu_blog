from django.urls import path
from .views import home_view, write_story

urlpatterns = [
    path('', home_view, name="home_view"),
    path('story/', write_story, name='story')
]