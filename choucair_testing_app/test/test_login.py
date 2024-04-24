from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class LoginApiTest(TestCase):
    def test_successful_login(self):
        # Create a test user
        self.username = 'Brian95'
        self.password = '12345'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        # Valid authentication data
        data = {"username": self.username, "password": self.password}
        # A login request
        response = self.client.post(reverse("login"), data)
        # Verifications
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('Token', response.json())

    def test_failed_login(self):
        # Inalid authentication data
        data = {"username": "Otto", "password": "34562"}
        # A login request
        response = self.client.post(reverse("login"), data)
        # Verifications
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual({'Message': 'The user does not exist'}, response.json())
