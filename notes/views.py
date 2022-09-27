import json
import logging
from pkgutil import get_data

from notes.models import Note
from rest_framework.views import APIView
from notes.serializers import NotesSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError 
from django.shortcuts import get_object_or_404

from notes.utils import verify_token
from user.models import User
from user.utils import JWTService

from notes.redis_crud import RedisNote

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='note.log', filemode='a', format=log, level=logging.DEBUG)


class NoteAppDetails(APIView):
    """
    create NoteAppdetails class
    """
    
    @verify_token
    def post(self, request):
        try:
            serializer = NotesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            createddata = RedisNote().set(serializer.data.get("user"), serializer.data)
            print('createddata', createddata)
            return Response({"message": "Note created", "redis_data": createddata}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @verify_token
    def get(self, request):
        try:
            user_id = request.data.get("user")
            
            notes_list = Note.objects.filter(user_id=request.data.get("user"))
            serializer = NotesSerializers(notes_list, many=True)
            if not serializer.data:
                raise Exception("Wrong credentials")
            get_data = RedisNote().get(user_id)
            print(get_data)

            return Response({"message": "Data retrieved", "redis_data": get_data.values()}, status=status.HTTP_200_OK)

        except ValidationError as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            
    @verify_token
    def put(self, request):
        try:
            note_object = Note.objects.get(id=request.data.get("id"))
            serializer = NotesSerializers(note_object, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_data = RedisNote().put(serializer.data)
            return Response({"message": "Update successful", "redis_data": updated_data}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @verify_token
    def delete(self, request):
        try:
            note_object = Note.objects.get(id=request.data.get("id"))
            RedisNote().delete(note_object)
            note_object.delete()
            return Response({"message": "Note deleted"}, status=status.HTTP_200_OK)

        except Exception as e:
            logging.exception(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            