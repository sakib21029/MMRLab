from django.urls import path
from . import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),


    # People
    path(
        "people/",
        views.people,
        name="people"
    ),


    # Publications
    path(
        "publications/",
        views.publications,
        name="publications"
    ),


    # Projects
    path(
        "projects/",
        views.projects,
        name="projects"
    ),


    # News
    path(
        "news/",
        views.news,
        name="news"
    ),


    # Collaborations
    path(
        "collaborations/",
        views.collaborations,
        name="collaborations"
    ),


    # Join Us
    path(
        "join-us/",
        views.join_us,
        name="join_us"
    ),

]