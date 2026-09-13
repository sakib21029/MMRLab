from django.shortcuts import render

from .models import (
    Supervisor,
    ResearchArea,
    Member,
    Project,
    Publication,
    News,
)


# =========================
# HOME PAGE
# =========================

def home(request):

    supervisor = Supervisor.objects.first()

    research_areas = ResearchArea.objects.all()

    members = Member.objects.all()[:6]

    projects = Project.objects.all()[:3]

    publications = Publication.objects.all()[:5]

    news = News.objects.all()[:3]


    context = {

        "supervisor": supervisor,

        "research_areas": research_areas,

        "members": members,

        "projects": projects,

        "publications": publications,

        "news": news,

    }


    return render(
        request,
        "home.html",
        context
    )



# =========================
# PEOPLE PAGE
# =========================

def people(request):

    members = Member.objects.all()

    context = {
        "members": members,
    }

    return render(
        request,
        "people.html",
        context
    )



# =========================
# PUBLICATIONS PAGE
# =========================

def publications(request):

    publications_list = Publication.objects.all().order_by("-year")

    context = {
        "publications": publications_list,
    }

    return render(
        request,
        "publications.html",
        context
    )



# =========================
# PROJECTS PAGE
# =========================

def projects(request):

    projects_list = Project.objects.all()

    context = {
        "projects": projects_list,
    }

    return render(
        request,
        "projects.html",
        context
    )



# =========================
# NEWS PAGE
# =========================

def news(request):

    news_list = News.objects.all()

    context = {
        "news": news_list,
    }

    return render(
        request,
        "news.html",
        context
    )



# =========================
# COLLABORATIONS PAGE
# =========================

def collaborations(request):

    return render(
        request,
        "collaborations.html"
    )



# =========================
# JOIN US PAGE
# =========================

def join_us(request):

    return render(
        request,
        "join_us.html"
    )