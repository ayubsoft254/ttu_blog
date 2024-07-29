from django.urls import path
from django.conf import settings
from .views import home_view, write_story
from posts.views import story, opinion, story_detail
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name="home_view"),
    path('story/', write_story, name='story'),
    path('stories/', story, name='stories'),
    path('stories/<int:pk>/', story_detail, name='story_detail'),
    path('opinions/', opinion, name='opinions'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)