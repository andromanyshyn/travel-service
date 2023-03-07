from django import forms
from .models import *


class FindWaybillForm(forms.ModelForm):
    class Meta:
        model = Waybills
        fields = ['start_point', 'end_point', 'max_road_time']


class LocalizationCreateForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = ['name']


class TransportCreateForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['code_name', 'waybill', 'road_time']


class WaybillCreateForm(forms.ModelForm):
    class Meta:
        model = Waybills
        fields = ['start_point', 'end_point', 'max_road_time']
