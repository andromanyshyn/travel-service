import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_service.settings')

import django

django.setup()

from django.test import TestCase
from django.urls import reverse

from .models import *


class IndexTestView(TestCase):
    fixtures = ['waybills.json', 'transports.json', 'localizations.json']

    def setUp(self):
        self.path = reverse('index')
        self.data_correct = {
            'start_point': 1,
            'end_point': 2,
            'max_road_time': 200,
        }
        self.data_incorrect = {
            'start_point': 223,
            'end_point': 145,
            'max_road_time': 1,
        }
        self.data_incorrect_time = {
            'start_point': 1,
            'end_point': 2,
            'max_road_time': 1,
        }
        self.data_incorrect_localizations = {
            'start_point': 500,
            'end_point': 500,
            'max_road_time': 50,
        }
        self.waybill_exists = Waybills.objects.filter(start_point=self.data_correct['start_point'],
                                                      end_point=self.data_correct['end_point'],
                                                      max_road_time__lte=self.data_correct['max_road_time'])
        self.waybill_not_exists = Waybills.objects.filter(start_point=self.data_incorrect['start_point'],
                                                          end_point=self.data_incorrect['end_point'],
                                                          max_road_time__lte=self.data_incorrect['max_road_time'])

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/index.html')

    def test_view_post_success(self):
        response = self.client.post(self.path, data=self.data_correct)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.waybill_exists)

    def test_view_post_errors(self):
        response = self.client.post(self.path, data=self.data_incorrect)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.waybill_not_exists.exists())

    def test_view_post_messages(self):
        response = self.client.post(self.path, data=self.data_incorrect_time)
        self.assertContains(response, 'The travel time is longer than the one you selected. Change the time')


class AllLocalizationsTestView(TestCase):
    fixtures = ['localizations.json']

    def setUp(self):
        self.path = reverse('localizations')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/localizations.html')
        self.assertEqual(list(response.context_data['object_list']), list(Localization.objects.all()[:5]))


class AllTransportsTestView(TestCase):
    fixtures = ['transports.json', 'waybills.json', 'localizations.json']

    def setUp(self):
        self.path = reverse('transports')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/transports.html')
        self.assertEqual(list(response.context_data['object_list']), list(Transport.objects.all()[:5]))


class AllWaybillsTestView(TestCase):
    fixtures = ['transports.json', 'waybills.json', 'localizations.json']

    def setUp(self):
        self.path = reverse('waybills')

    def test_view_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_function/waybills.html')
        self.assertEqual(list(response.context_data['object_list']), list(Waybills.objects.all()[:5]))
