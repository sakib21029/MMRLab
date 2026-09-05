from django.urls import path
from .views import (
    home, 
    create_admin, 
    publications, 
    people, 
    join_us
)

urlpatterns = [
    path("", home, name="home"),
    path("create-admin/", create_admin, name="create_admin"),
    
    # Add routes for the missing pages:
    path("publications/", publications, name="publications"),
    path("people/", people, name="people"),
    path("join-us/", join_us, name="join_us"),
]