from django.shortcuts import render

from .models import (
    Supervisor,
    LabMember,
    ResearchArea,
    Project,
    Publication,
    News,
    Collaboration
)



# Homepage

def home(request):

    supervisor = Supervisor.objects.first()

    research_areas = ResearchArea.objects.all()

    projects = Project.objects.all()[:3]

    publications = Publication.objects.all()[:5]

    news = News.objects.all()[:3]

    members = LabMember.objects.all()[:6]


    context = {

        "supervisor": supervisor,

        "research_areas": research_areas,

        "projects": projects,

        "publications": publications,

        "news": news,

        "members": members,

    }


    return render(
        request,
        "home.html",
        context
    )





# People Page

def people(request):

    collaborators = LabMember.objects.filter(
        role="research_collaborator"
    )


    assistants = LabMember.objects.filter(
        role="research_assistant"
    )


    junior_assistants = LabMember.objects.filter(
        role="junior_research_assistant"
    )


    alumni = LabMember.objects.filter(
        role="alumni"
    )


    context = {

        "collaborators": collaborators,

        "assistants": assistants,

        "junior_assistants": junior_assistants,

        "alumni": alumni,

    }


    return render(
        request,
        "people.html",
        context
    )





# Publications Page

def publications(request):

    papers = Publication.objects.all().order_by(
        '-year'
    )


    return render(
        request,
        "publications.html",
        {
            "publications": papers
        }
    )





# Projects Page

def projects(request):

    project_list = Project.objects.all()


    return render(
        request,
        "projects.html",
        {
            "projects": project_list
        }
    )





# News Page

def news(request):

    news_list = News.objects.all().order_by(
        '-date'
    )


    return render(
        request,
        "news.html",
        {
            "news": news_list
        }
    )





# Join Us Page

def join_us(request):

    return render(
        request,
        "join_us.html"
    )





# Collaboration Page

def collaborations(request):

    partners = Collaboration.objects.all()


    return render(
        request,
        "collaborations.html",
        {
            "collaborations": partners
        }
    )