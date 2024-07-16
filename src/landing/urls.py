from django.urls import path
from landing.views import home_view

urlpatterns = [
    path('', home_view, name="home_view"),
]