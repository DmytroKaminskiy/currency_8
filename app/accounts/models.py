from django.contrib.auth.models import AbstractUser
from django.db import models, DataError


def user_avatar(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # email = models.EmailField(_("email address"), blank=True)
    email = models.EmailField('email address', unique=True)
    avatar = models.FileField(upload_to=user_avatar)
    email_internal = models.EmailField()
    # active_avatar = models.ForeignKey('accounts.Avatar', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # self.first_name = self.first_name.capitalize()
        # self.last_name = self.last_name.capitalize()
        # self._clean_email()

        # check_queryset = self.__class__.objects.filter(email_internal=self.email_internal)
        # if self.id:
        #     check_queryset = check_queryset.exclude(id=self.id)
        # if check_queryset.exists():
        #     raise DataError("Email already exists.")

        print('Before Save')
        super().save(*args, **kwargs)
        print('After Save')

    def _clean_email(self):
        # TODO if email was changed!
        email_username, email_domain = self.email.split('@')
        if not email_username.isalnum():
            self.email_internal = ''.join(char for char in email_username if char.isalnum()) + \
                f'@{email_domain}'

# class Avatar(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
#     image = models.ImageField()
    # is_active = models.BooleanField(default=False)


'''
1. SignUp form - email, password, confirm_password -> send email with `activation link` | create user as `non active`
2. User clicks link in email, make user as `active`.
'''