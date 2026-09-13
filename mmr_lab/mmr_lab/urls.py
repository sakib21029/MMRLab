from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "people/",
        views.people,
        name="people"
    ),

    path(
        "publications/",
        views.publications,
        name="publications"
    ),

    path(
        "projects/",
        views.projects,
        name="projects"
    ),

    path(
        "news/",
        views.news,
        name="news"
    ),

    path(
        "collaborations/",
        views.collaborations,
        name="collaborations"
    ),

    path(
        "join-us/",
        views.join_us,
        name="join_us"
    ),

]