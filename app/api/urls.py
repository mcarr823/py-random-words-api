from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("word/", views.random, name="random"),
    path("word/<int:length>/", views.randomLength, name="randomLength"),
    path("words/", views.all, name="all"),
    path("words/<int:length>/", views.allLength, name="allLength"),
]