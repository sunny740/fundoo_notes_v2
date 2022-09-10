import logging

from notes.models import Note
from rest_framework.views import APIView
from notes.serializers import NotesSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError 
from django.shortcuts import get_object_or_404


log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='note.log', filemode='a', format=log, level=logging.DEBUG)


class NoteAppDetails(APIView):

    def get(self, request):
        try:
            notes = Note.objects.filter(user=request.data.get("user"))
            serializer = NotesSerializers(instance=notes, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            logging.exception(e)
            return Response({'message': e.detail}, status=400)
            
        except Exception as e:
            logging.exception(e)
            return Response({'message': str(e)}, status=400)

    def post(self, request):
        try:
            serializer = NotesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": f"Data save successfully","data": serializer.data}, status.HTTP_201_CREATED)
        except ValidationError as e:
            logging.exception(e)
            return Response({'message': e.detail}, status=400)

        except Exception as e:
            logging.exception(e)
            print(e)
            return Response({"message": "Unexpected error"}, status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            note = get_object_or_404(Note,id=request.data.get('id'))
            
            serializer = NotesSerializers(note, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data}, status = status.HTTP_202_ACCEPTED)

        except Exception as e:
            logging.exception(e)
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            notes.delete()
            return Response({'data': 'deleted'}, status = 204)
        except ValidationError as e:
            logging.exception(e)
            return Response({'message': e.detail}, status=400)

        except Exception as e:
            logging.exception(e)
            return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)
