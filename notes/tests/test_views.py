from importlib.resources import contents
from urllib import request
import pytest
import json
from django.urls import reverse


class TestNoteAppDetails:


    # @pytest.mark.crud
    @pytest.mark.django_db

    def test_create_crud_operations_notes(self, client, django_user_model, db):

        user = django_user_model.objects.create_user(username="sunny", password="12345", first_name="sunny",
                                                 last_name="Sejwar", email="sunny12@gmail.com",
                                                 phone_number=987671365, location="MP", is_verified=True)

        header = {"content_type": "application/json", "HTTP_TOKEN": user.tokens()}
        url = reverse('registration')
        
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language"}
        url = reverse('notes')
        response = client.post(url, data,**header)
        assert response.status_code == 201

    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_get_ope(self, client, django_user_model, db):
        
        user = django_user_model.objects.create_user(username="sunny", password="12345", first_name="sunny",
                                                 last_name="Sejwar", email="sunny12@gmail.com",
                                                 phone_number=987671365, location="MP", is_verified=True)
             
        header = {"content_type": "application/json", "HTTP_TOKEN": user.tokens()}
        
        url = reverse('registration')

        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language"}
        url = reverse('notes')
        post_response = client.post(url,data, **header )
        assert post_response.status_code == 201

        getresponse = client.get(url,data, **header)
        assert getresponse.status_code == 200


    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_delete_crud_operations_notes(self, client, django_user_model, db):

        user = django_user_model.objects.create_user(username="sunny", password="12345", first_name="sunny",
                                                 last_name="Sejwar", email="sunny12@gmail.com",
                                                 phone_number=987671365, location="MP", is_verified=True)
        url = reverse('registration')       
        
        header = {"content_type": "application/json", "HTTP_TOKEN": user.tokens()}
        
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language"}
        url = reverse('notes')
        
        post_response = client.post(url, data, **header)

        assert post_response.status_code == 201
        note_id = post_response.data.get('data').get('id')
        delete_response = client.delete(url, {"id": note_id}, **header)
        assert delete_response.status_code == 200


    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_put_crud_operations_notes(self, client, django_user_model):

        user = django_user_model.objects.create_user(username="sunny", password="12345", first_name="sunny",
                                                 last_name="Sejwar", email="sunny12@gmail.com",
                                                 phone_number=987671365, location="MP", is_verified=True)
        url = reverse('registration')

        header = {"content_type": "application/json", "HTTP_TOKEN": user.tokens()}
        
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language"}
        url = reverse('notes')
        
        response = client.post(url, data,**header)
        noteid = response.data.get('data').get('id')
        assert response.status_code == 201
        
        getresponse = client.get(url,data, **header)       
        assert getresponse.status_code == 200

        data1 = {"id" : noteid ,"title": "Python", "description": "Interpreted & high label Programming Language"}
        response = client.put(url, data1, **header)
        assert response.status_code == 202

