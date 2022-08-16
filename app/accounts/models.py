from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # email = models.EmailField(_("email address"), blank=True)
    email = models.EmailField('email address', unique=True)


'''
1. SignUp form - email, password, confirm_password -> send email with `activation link` | create user as `non active`
2. User clicks link in email, make user as `active`.
'''