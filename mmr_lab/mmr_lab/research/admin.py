from django.contrib import admin

from .models import (
    Supervisor,
    LabMember,
    ResearchArea,
    Project,
    Publication,
    News,
    Collaboration
)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'designation'
    )



@admin.register(LabMember)
class LabMemberAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'role',
        'current_affiliation'
    )

    list_filter = (
        'role',
    )

    search_fields = (
        'name',
        'research_interest'
    )



@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):

    list_display = (
        'title',
    )



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'status',
    )

    list_filter = (
        'status',
    )



@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'journal',
        'year'
    )



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date'
    )



@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):

    list_display = (
        'institution',
        'country'
    )