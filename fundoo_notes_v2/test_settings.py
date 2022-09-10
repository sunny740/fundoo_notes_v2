"""
"""
# from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fundoo_notes_v2',
        'USER': 'postgres',
        'PASSWORD': 'Sunny@123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backend.locmem.EmailBackend'