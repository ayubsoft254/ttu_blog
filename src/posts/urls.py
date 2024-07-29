from django.urls import path
from .views import  post_story, post_opinion, story_list, story_detail, opinion_list, opinion_detail, comment_on_post, like_post

urlpatterns = [
    path('stories/', story_list, name='story_list'),
    path('stories/post/', post_story, name='post_story'),
    path('stories/<int:pk>/',story_detail, name='story_detail'),
    path('opinions/', opinion_list, name='opinion_list'),
    path('opinions/post/',post_opinion, name='post_opinion'),
    path('opinions/<int:pk>/',opinion_detail, name='opinion_detail'),
    path('comments/<int:content_type_id>/<int:object_id>/', comment_on_post, name='comment_on_post'),
    path('likes/<int:content_type_id>/<int:object_id>/',like_post, name='like_post'),
]
