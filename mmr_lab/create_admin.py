import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mmr_lab.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

try:
    user = User.objects.get(username="admin")
    print("Existing admin found")
except User.DoesNotExist:
    user = User.objects.create_user(
        username="admin",
        email="sakib.towhidujjaman@gmail.com",
        password="mmrlab@123"
    )
    print("New admin created")

user.set_password("mmrlab@123")
user.is_staff = True
user.is_superuser = True
user.save()

print("DONE:", user.username)