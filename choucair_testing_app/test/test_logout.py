from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class LogoutApiTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()

        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        result = response.json()
        self.access_token = result["Token"]

    def test_successful_logout(self):
        data = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(
            reverse('logout'),
            data,
            HTTP_AUTHORIZATION='Token ' + self.access_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual({'Mesage': 'The logout was successful'}, response.json())

    def test_failed_logout(self):
        data = {
            "username": "test",
            "password": "12345"
        }
        response = self.client.post(
            reverse('logout'),
            data,
            HTTP_AUTHORIZATION='Token ' + self.access_token
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual({'Message': 'The user does not exist'}, response.json())
