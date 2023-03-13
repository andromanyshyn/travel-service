import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_service.settings')

import django

django.setup()

from django.test import TestCase
from django.urls import reverse
from .models import *


class IndexTestView(TestCase):
    def setUp(self):
        self.path = reverse('index')
        self.data_correct = {
            'start_point': 1,
            'end_point': 2,
            'max_road_time': 200,
        }
        self.data_incorrect = {
            'start_point': 1,
            'end_point': 2,
            'max_road_time': 1,
        }

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/index.html')

    def test_view_post_success(self):
        response = self.client.post(self.path, data=self.data_correct)
        self.assertEqual(response.status_code, 302)

    def test_view_post_errors(self):
        response = self.client.post(self.path, data=self.data_incorrect)
        self.assertEqual(response.status_code, 302)


class AllLocalizationsTestView(TestCase):
    fixtures = ['localization.json']

    def setUp(self):
        self.path = reverse('localizations')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/localizations.html')
        self.assertEqual(list(response.context_data['object_list']), list(Localization.objects.all()))


class AllTransportsTestView(TestCase):
    fixtures = ['transport.json', 'waybill.json', 'localization.json']

    def setUp(self):
        self.path = reverse('transports')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/transports.html')
        self.assertEqual(list(response.context_data['object_list']), list(Transport.objects.all()))


class AllWaybillsTestView(TestCase):
    fixtures = ['transport.json', 'waybill.json', 'localization.json']

    def setUp(self):
        self.path = reverse('waybills')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/waybills.html')
        self.assertEqual(list(response.context_data['object_list']), list(Waybills.objects.all()))
