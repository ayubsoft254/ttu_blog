from django.urls import path
from .views import home_view, stories, k_pop_queerbating, open_relationships, open_relationships_101
from posts.views import story, opinion

urlpatterns = [
    path('', home_view, name='home_view'),
    path('write_story/', stories, name='stories'),
    path('k-pop-queerbating/', k_pop_queerbating, name='k_pop_queerbating'),
    path('tag/open-relationships/', open_relationships, name='open_relationships'),
    path('open-relationships-101/', open_relationships_101, name='open_relationships_101'),
    path('story/', story, name='story'),
    path('opinions/', opinion, name='opinions')
]
