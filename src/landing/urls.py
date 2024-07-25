from django.urls import path
from .views import home_view, write_story
from posts.views import story, opinion

urlpatterns = [
    path('', home_view, name="home_view"),
    path('story/', write_story, name='story'),
    path('stories/', story, name='stories'),
    path('opinions/', opinion, name='opinions'),

]