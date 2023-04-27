from django.urls import path

from . import views

urlpatterns = [

    path("", views.home_page, name="home_page"),
    path("states/", views.state_queries, name="state_queries"),
    path("india/", views.india_queries, name="india_queries"),
    path("world/", views.world_queries, name="world_queries"),

]