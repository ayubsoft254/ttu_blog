from django.urls import path
from .views import home_view, write_story, k_pop_queerbating, open_relationships
from landing.views import story, opinion  # Ensure this is correct

urlpatterns = [
    path('', home_view, name='home_view'),
    path('write_story/', write_story, name='stories'),
    path('k-pop-queerbating/', k_pop_queerbating, name='k_pop_queerbating'),
    path('tag/open-relationships/', open_relationships, name='open_relationships'),
    path('story/', story, name='story'),
    path('opinions/', opinion, name='opinions')
]
