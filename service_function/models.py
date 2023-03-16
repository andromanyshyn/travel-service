from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import models


class Localization(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)

    class Meta:
        verbose_name_plural = 'Localizations'

        ordering = ['name']

    def __str__(self):
        return self.name


class Transport(models.Model):
    code_name = models.UUIDField(unique=True, null=False)
    waybill = models.ForeignKey(to='Waybills', on_delete=models.CASCADE, blank=True, null=True)
    road_time = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Transports'
        ordering = ['road_time']

    def __str__(self):
        return str(self.code_name)


class Waybills(models.Model):
    start_point = models.ForeignKey(to=Localization, related_name='start_point', on_delete=models.CASCADE)
    end_point = models.ForeignKey(to=Localization, related_name='end_point', on_delete=models.CASCADE)
    max_road_time = models.PositiveIntegerField(null=True)
    towns = models.ManyToManyField(to=Localization, blank=True)

    class Meta:
        verbose_name_plural = 'Waybils'
        ordering = ['max_road_time']

    class Meta:
        verbose_name_plural = 'Waybils'

    def __str__(self):
        return f'{self.start_point} - {self.end_point} | {self.max_road_time} minutes road'


class SavedWaybills(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
