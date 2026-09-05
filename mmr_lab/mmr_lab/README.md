# MMR Lab Website

## Molecular & Microbiology Research Laboratory


A Django-based research laboratory website designed for managing research activities, team members, publications, projects, news, and collaborations.


## Features

- Supervisor profile management
- Research areas showcase
- Research team profiles
- Research assistants and alumni profiles
- Publications management
- Research project management
- Laboratory news and updates
- Collaboration information
- Join Us application form
- Responsive design for desktop, tablet, and mobile


## Technology Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- SQLite Database


## Installation Guide


### 1. Clone Repository

```bash
git clone your-github-repository-link
### 2. Create Virtual Environment
python -m venv venv
###3. Activate Virtual Environment

Windows:

venv\Scripts\activate
###4. Install Required Packages
pip install -r requirements.txt
###5. Database Setup
python manage.py migrate
###6. Create Admin Account
python manage.py createsuperuser
###7. Run Development Server
python manage.py runserver

Open your browser:

http://127.0.0.1:8000/