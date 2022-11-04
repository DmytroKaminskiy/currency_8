from .settings import *

# print(globals())

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
