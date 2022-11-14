from accounts.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



@receiver(pre_save, sender=User)
def before_save_first_name_user(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=User)
def before_save_last_name_user(sender, instance, **kwargs):
    instance.last_name = instance.last_name.capitalize()


# @receiver(post_save, sender=User)
# def after_save_user(sender, instance, **kwargs):
#     print('AFTER SAVE SIGNAL')
