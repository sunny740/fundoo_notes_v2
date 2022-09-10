import pytest
import json
from django.urls import reverse

class TestRegisterAPI:
    """
    create the test class and 
    """
    
    @pytest.mark.django_db
    def test_response_as_registration_successfull(self, client):

        # Create user
        url = reverse('registration')
        # Registration succesfull
        data = {'first_name': 'Monu', 'last_name': 'Khanna', 'email': 'monu0287@gmail.com', 'username': 'Monu0287', 'password': '7777', 'phone_number':7996541230, 'location': "gwalior"}
        response = client.post(url, data)
        assert response.status_code == 201
        json_data = json.loads(response.content)
        assert json_data['data']['username'] == 'Monu0287'
        assert json_data['data']['username'] != 'User Monu0287 is successfully login'


    @pytest.mark.django_db
    def test_invalid_as_registration_successfull(self, client):

        url = reverse('registration')
        
        data = {'first_name': 'Monu', 'last_name': 'Khanna','password': '7777', 'phone_number':7996541230, 'location': "gwalior"}
        response = client.post(url, data)
        assert response.status_code == 400


    @pytest.mark.django_db
    def test_response_as_login_successfull(self, client, django_user_model):

        # Create user
        django_user_model.objects.create_user(username='sunny123', first_name = 'sunny', last_name = 'sejwar', email = 'sunny123@gmail.com', password='Sunny@123', phone_number=1234567890,
                                              location='MP')
        url = reverse('login')
        
        data = {'username': 'sunny123', 'password': 'Sunny@123'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 202


    @pytest.mark.django_db
    def test_invalid_user_login(self, client, django_user_model):

        django_user_model.objects.create_user(username='sunny123', first_name = 'sunny', last_name = 'sejwar',
                email = 'sunny123@gmail.com', password='Sunny@123', phone_number=1234567890, location='MP')

        url = reverse('login')
        # Login failed
        data = {'username': 'sunny', 'password': 'Sunny@123'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 400
        assert response.data['message'] == 'Invalid Credentials'
