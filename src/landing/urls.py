from django.urls import path
from .views import home_view, stories, k_pop_queerbating, open_relationships, open_relationships_101, tag_stories, author_stamos, author_ilya, author_menenaba, author_anonymous, author_questionmike
from posts.views import story, opinion

urlpatterns = [
    path('', home_view, name='home_view'),
    path('write_story/', stories, name='stories'),
    path('k-pop-queerbating/', k_pop_queerbating, name='k_pop_queerbating'),
    path('tag/open-relationships/', open_relationships, name='open_relationships'),
    path('open-relationships-101/', open_relationships_101, name='open_relationships_101'),
    path('story/', story, name='story'),
    path('opinions/', opinion, name='opinions'),
    path('tag/stories/', tag_stories, name='tag_stories'),
    path('author/stamos/', author_stamos, name='author_stamos'),
    path('author/ilya/', author_ilya, name='author_ilya'),
    path('author/menenaba/', author_menenaba, name='author_menenaba'),
    path('author/anonymous/', author_anonymous, name='author_anonymous'),
    path('author/questionmike/', author_questionmike, name='author_questionmike')
]
