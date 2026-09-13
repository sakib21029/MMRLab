from django.shortcuts import render

from .models import (
    Supervisor,
    ResearchArea,
    Member,
    Project,
    Publication,
    News,
)


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


def people(request):

    members = Member.objects.all()

    return render(
        request,
        "people.html",
        {
            "members": members
        }
    )


def publications(request):

    publications_list = Publication.objects.all().order_by("-year")

    return render(
        request,
        "publications.html",
        {
            "publications": publications_list
        }
    )


def projects(request):

    projects_list = Project.objects.all()

    return render(
        request,
        "projects.html",
        {
            "projects": projects_list
        }
    )


def news(request):

    news_list = News.objects.all()

    return render(
        request,
        "news.html",
        {
            "news": news_list
        }
    )


def collaborations(request):

    return render(
        request,
        "collaborations.html"
    )


def join_us(request):

    return render(
        request,
        "join_us.html"
    )