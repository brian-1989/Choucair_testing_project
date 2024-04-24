from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from pathlib import Path
import os

class GetProductApiTest(TestCase):
    def setUp(self):
        # Creat a test user
        self.username = 'Brian95'
        self.password = '12345'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user.save()

        # Creat a test token
        response = self.client.post(
            reverse('login'), {'username': self.username, 'password': self.password})
        result = response.json()
        self.access_token = result["Token"]

        # Creat a test product
        with open(os.path.join(Path(__file__).resolve().parent.parent.parent, "media/product image/Cellphone.png"), "rb") as image_file:
            data = {
                "product_name": "Cellphone",
                "description": "Electric device",
                "price": 12000,
                "stock": 2,
                "product_image": image_file
            }
            response = self.client.post(
                reverse('create_product'),
                data,
                HTTP_AUTHORIZATION='Token ' + self.access_token
            )
            result = response.json()
            self.product_id = result["product_id"]

    def test_successful_get_product(self):
        response = self.client.get(
            reverse('get_product'),
            {"product_id": self.product_id},
            HTTP_AUTHORIZATION='Token ' + self.access_token
        )
        product_information = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product_information, response.json())

    def test_failed_get_product(self):
        response = self.client.get(
            reverse('get_product'),
            {"product_id": "test"},
            HTTP_AUTHORIZATION='Token ' + self.access_token
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateProductApiTest(TestCase):
    def setUp(self):
        # Creat a test user
        self.username = 'Brian95'
        self.password = '12345'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user.save()

        # Creat a test token
        response = self.client.post(
            reverse('login'), {'username': self.username, 'password': self.password})
        result = response.json()
        self.access_token = result["Token"]

    def test_successful_create_product(self):
        with open(os.path.join(Path(__file__).resolve().parent.parent.parent, "media/product image/Cellphone.png"), "rb") as image_file:
            data = {
                "product_name": "Cellphone",
                "description": "Electric device",
                "price": 12000,
                "stock": 2,
                "product_image": image_file
            }
            response = self.client.post(
                reverse('create_product'),
                data,
                HTTP_AUTHORIZATION='Token ' + self.access_token
            )
            product_information = response.json()
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(product_information, response.json())


class DeleteProductApiTest(TestCase):
    def setUp(self):
        # Creat a test user
        self.username = 'Brian95'
        self.password = '12345'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user.save()

        # Creat a test token
        response = self.client.post(
            reverse('login'), {'username': self.username, 'password': self.password})
        result = response.json()
        self.access_token = result["Token"]

        # Creat a test product
        with open(os.path.join(Path(__file__).resolve().parent.parent.parent, "media/product image/Cellphone.png"), "rb") as image_file:
            data = {
                "product_name": "Cellphone",
                "description": "Electric device",
                "price": 12000,
                "stock": 2,
                "product_image": image_file
            }
            response = self.client.post(
                reverse('create_product'),
                data,
                HTTP_AUTHORIZATION='Token ' + self.access_token
            )
            result = response.json()
            self.product_id = result["product_id"]

    def test_successful_delete_product(self):
        print(f"self.product_id: {self.product_id}")
        response = self.client.delete(
            f"/api/delete_product/?product_id={self.product_id}",
            HTTP_AUTHORIZATION='Token ' + self.access_token
        )
        product_information = response.status_code
        print(f"product_information: {product_information}")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
