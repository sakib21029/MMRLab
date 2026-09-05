from .models import LabMember


def team_members(request):

    assistants = LabMember.objects.filter(
        role="research_assistant"
    )


    alumni = LabMember.objects.filter(
        role="alumni"
    )


    return {

        "assistants": assistants,

        "alumni": alumni,

    }