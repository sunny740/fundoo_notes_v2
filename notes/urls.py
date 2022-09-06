from django.urls import path
from .views import NoteAppDetails

urlpatterns = [
    path('notes', NoteAppDetails.as_view(), name="notes"),
]