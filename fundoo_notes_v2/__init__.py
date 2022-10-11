# fundoo_notes_v2/__init__.py

from .celery import app as celery_app

__all__ = ("celery_app",)