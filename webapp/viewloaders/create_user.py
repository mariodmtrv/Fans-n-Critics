__author__ = 'mario-dimitrov'
from django.contrib.auth.models import User


def create_user(username, password, password_confirmation, email,
                first_name, last_name):
    if password and username and email and password == password_confirmation:
        count = User.objects.filter(username=username).count()
        if count > 0:
            return False
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return True
        return False
