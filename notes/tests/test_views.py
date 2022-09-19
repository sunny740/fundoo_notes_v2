from importlib.resources import contents
import pytest
import json
from django.urls import reverse

class TestNoteAppDetails:


    # @pytest.mark.crud
    @pytest.mark.django_db

    def test_create_crud_operations_notes(self, client):

        url = reverse('registration')
        data = {'first_name': 'Monu', 'last_name': 'Khanna', 'email': 'monu0287@gmail.com', 'username': 'Monu0287', 'password': '7777', 'phone_number':7996541230, 'location': "gwalior"}

        response = client.post(url, data, content_type = "application/json")
        user_data = json.loads(response.content)
        # print(user_data)
        user_id = user_data.get("data").get("id")
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language", "user" : user_id}
        url = reverse('notes')
        response = client.post(url, data)
        assert response.status_code == 201

    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_get_ope(self, client):
        
        url = reverse('registration')
        data = {'first_name': 'Monu', 'last_name': 'Khanna', 'email': 'monu0287@gmail.com', 'username': 'Monu0287', 'password': '7777', 'phone_number':7996541230, 'location': "gwalior"}
        
        response = client.post(url, data, content_type = "application/json")
        assert response.status_code == 201
        user_id = response.data.get('data').get('id')        
        url = reverse('notes')
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language", "user" :user_id}
        post_response = client.post(url,data )
        assert post_response.status_code == 201
        getresponce = client.get(url,{'user': user_id}, content_type = "application/json")
        assert getresponce.status_code == 200

    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_delete_crud_operations_notes(self, client):

        url = reverse('registration')       
        data = {'first_name': 'Monu', 'last_name': 'Khanna', 'email': 'monu0287@gmail.com', 'username': 'Monu0287', 'password': '7777', 'phone_number':7996541230, 'location': "gwalior"}

        response = client.post(url, data, content_type = "application/json")
        user_data = json.loads(response.content)
        # print(user_data)
        user_id = user_data.get("data").get("id")
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Language", "user" :user_id}
        url = reverse('notes')
        response = client.post(url, data)
        assert response.status_code == 201
        # print(response.data)
        note_id = response.data.get('data').get('id')
        # print(note_id)
        delete_response = client.delete(url, {"id": note_id}, content_type = "application/json")
        print(delete_response.data)
        assert delete_response.status_code == 204


    # @pytest.mark.crud
    @pytest.mark.django_db
    def test_put_crud_operations_notes(self, client):

        url = reverse('registration')
        
        data = {'first_name': 'Monu', 'last_name': 'Khanna', 'email': 'monu0287@gmail.com', 'username': 'Monu0287', 'password': '7777', 'phone_number':7996541230, 'location': "gwalior"}
        response = client.post(url, data)
        json_data = json.loads(response.content)
        user_id = json_data['data']['id']
        url1 = reverse('notes')
        data = {"title": "PythonLanguage", "description": "Interpreted & high label Programming Language", "user" :user_id}
        response = client.post(url1, data)
        json_data = json.loads(response.content)
        print(json_data)
    
        note_id = json_data['data']['id']
        assert response.status_code == 201
        data1 = json.dumps({"id" : note_id,"title": "Python", "description": "Interpreted & high label Programming Language", "user" :user_id})
        response = client.put(url1,data1,content_type = "application/json")
        assert response.status_code == 202

        