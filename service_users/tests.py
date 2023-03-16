import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_service.settings')

import django

django.setup()

from django.test import TestCase
from django.urls import reverse

from .models import *


class RegistrationTestView(TestCase):
    def setUp(self):
        self.path = reverse('registration')
        self.user_exists = User.objects.create(username='moriss123',
                                               email='moriss1@gmail.com',
                                               password='a9517535')
        self.data = {
            'username': 'moriss123',
            'email': 'moriss1@gmail.com',
            'password1': 'a9517535',
            'password2': 'a9517535',
        }

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_users/registration.html')

    def test_view_post(self):
        username = self.data['username']
        self.assertTrue(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, data=self.data)
        self.assertEqual(response.status_code, 200)


class LoginTestView(TestCase):
    def setUp(self):
        self.path = reverse('login')
        self.data = {
            'username': 'moris',
            'password': 'a9517535',
        }

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_users/login.html')

    def test_view_post(self):
        username = self.data['username']

        self.assertFalse(User.objects.filter(username=username).exists())
        self.user = User.objects.create(username='moris',
                                        email='moris123@gmail.com',
                                        password='a9517535')
        self.assertTrue(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, data=self.data)
        self.assertEqual(response.status_code, 200)
