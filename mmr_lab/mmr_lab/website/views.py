from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Import models from your app (adjust model names if your models differ)
from .models import (
    Supervisor,
    ResearchArea,
    Member,
    Project,
    Publication,
    News,
)


def home(request):
    # Fetch data to populate home.html
    supervisor = Supervisor.objects.first() if hasattr(Supervisor, 'objects') else None
    research_areas = ResearchArea.objects.all() if hasattr(ResearchArea, 'objects') else []
    members = Member.objects.all()[:6] if hasattr(Member, 'objects') else []
    projects = Project.objects.all()[:3] if hasattr(Project, 'objects') else []
    publications = Publication.objects.all()[:5] if hasattr(Publication, 'objects') else []
    news = News.objects.all()[:3] if hasattr(News, 'objects') else []

    context = {
        "supervisor": supervisor,
        "research_areas": research_areas,
        "members": members,
        "projects": projects,
        "publications": publications,
        "news": news,
    }
    return render(request, "home.html", context)


def publications(request):
    publications_list = Publication.objects.all().order_by("-year") if hasattr(Publication, 'objects') else []
    return render(request, "publications.html", {"publications": publications_list})


def people(request):
    members = Member.objects.all() if hasattr(Member, 'objects') else []
    return render(request, "people.html", {"members": members})


def join_us(request):
    return render(request, "join_us.html")


def create_admin(request):
    User = get_user_model()

    user, created = User.objects.get_or_create(
        username="admin",
        defaults={
            "email": "sakib.towhidujjaman@gmail.com"
        }
    )

    user.set_password("mmrlab@123")
    user.is_staff = True
    user.is_superuser = True
    user.save()

    return HttpResponse("Admin created successfully")