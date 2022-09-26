from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatar(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # email = models.EmailField(_("email address"), blank=True)
    email = models.EmailField('email address', unique=True)
    avatar = models.FileField(upload_to=user_avatar)
    # active_avatar = models.ForeignKey('accounts.Avatar', on_delete=models.CASCADE)


# class Avatar(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
#     image = models.ImageField()
    # is_active = models.BooleanField(default=False)


'''
1. SignUp form - email, password, confirm_password -> send email with `activation link` | create user as `non active`
2. User clicks link in email, make user as `active`.
'''