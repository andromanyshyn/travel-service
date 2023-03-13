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
        response = self.client.post(self.path, data=self.data)
        self.assertEqual(response.status_code, 302)


class LoginTestView(TestCase):
    def setUp(self):
        self.path = reverse('login')
        self.data = {
            'username': 'moriss123',
            'password': 'a9517535',
        }

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_users/login.html')

    def test_view_post(self):
        response = self.client.post(self.path, data=self.data)
        self.assertEqual(response.status_code, 200)
