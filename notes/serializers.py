from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from notes.models import Note

class NotesSerializers(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Note
        # fields =  '__all__'
        fields =  ['id', 'user', 'title', 'description']
    