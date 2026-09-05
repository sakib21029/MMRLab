from django.db import models


# Supervisor Profile

class Supervisor(models.Model):

    name = models.CharField(
        max_length=200
    )

    designation = models.CharField(
        max_length=200
    )

    bio = models.TextField()


    vision = models.TextField()


    mission = models.TextField()


    linkedin = models.URLField(
        blank=True
    )


    orcid = models.URLField(
        blank=True
    )


    google_scholar = models.URLField(
        blank=True
    )


    portfolio = models.URLField(
        blank=True
    )


    photo = models.ImageField(
        upload_to="supervisor/"
    )


    def __str__(self):

        return self.name
    # Lab Members

class LabMember(models.Model):


    ROLE_CHOICES = [

        ('research_collaborator',
         'Research Collaborator'),


        ('research_assistant',
         'Research Assistant'),


        ('junior_research_assistant',
         'Junior Research Assistant'),


        ('alumni',
         'Alumni'),

    ]


    name = models.CharField(
        max_length=200
    )


    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
    )


    designation = models.CharField(
        max_length=200,
        blank=True
    )


    education = models.CharField(
        max_length=300,
        blank=True
    )


    research_interest = models.TextField()


    biography = models.TextField()


    email = models.EmailField(
        blank=True
    )


    linkedin = models.URLField(
        blank=True
    )


    orcid = models.URLField(
        blank=True
    )


    google_scholar = models.URLField(
        blank=True
    )


    portfolio = models.URLField(
        blank=True
    )


    current_position = models.CharField(
        max_length=200,
        blank=True
    )


    current_affiliation = models.CharField(
        max_length=300,
        blank=True
    )


    photo = models.ImageField(
        upload_to="lab_members/"
    )


    def __str__(self):

        return self.name
    # Research Areas

class ResearchArea(models.Model):

    title = models.CharField(
        max_length=200
    )


    icon = models.CharField(
        max_length=50,
        help_text="Example: 🧬"
    )


    description = models.TextField()


    def __str__(self):

        return self.title
    # Research Projects

class Project(models.Model):

    STATUS_CHOICES = [

        ('ongoing', 'Ongoing'),

        ('completed', 'Completed'),

        ('future', 'Future Project'),

    ]


    title = models.CharField(
        max_length=300
    )


    research_area = models.ForeignKey(

        ResearchArea,

        on_delete=models.CASCADE

    )


    description = models.TextField()


    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES

    )


    start_date = models.DateField(

        blank=True,

        null=True

    )


    end_date = models.DateField(

        blank=True,

        null=True

    )


    def __str__(self):

        return self.title
    # Publications

class Publication(models.Model):


    title = models.CharField(
        max_length=500
    )


    authors = models.TextField()


    journal = models.CharField(
        max_length=300
    )


    year = models.IntegerField()


    doi = models.URLField(
        blank=True
    )


    abstract = models.TextField(
        blank=True
    )


    def __str__(self):

        return self.title
    # News and Updates

class News(models.Model):


    title = models.CharField(
        max_length=300
    )


    content = models.TextField()


    image = models.ImageField(

        upload_to="news/",

        blank=True

    )


    date = models.DateField(

        auto_now_add=True

    )


    def __str__(self):

        return self.title
    # Research Collaboration

class Collaboration(models.Model):


    institution = models.CharField(
        max_length=300
    )


    country = models.CharField(
        max_length=100
    )


    website = models.URLField(
        blank=True
    )


    logo = models.ImageField(

        upload_to="collaborations/",

        blank=True

    )


    description = models.TextField(
        blank=True
    )


    def __str__(self):

        return self.institution