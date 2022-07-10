from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index-file"),
    path('home', views.index, name="index-file"),
    path('index', views.index, name="index-file"),
    path('sports', views.sports, name="sports"),
    path('national', views.national, name="national"),
    path('business', views.business, name="business"),
    path('world', views.world, name="world"),
    path('politics', views.politics, name="politics"),
    path('technology', views.technology, name="technology"),
    path('entertainment', views.entertainment, name="entertainment"),
]
