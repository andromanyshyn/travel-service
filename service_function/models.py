import uuid

from django.db import models


class Localization(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)

    def __str__(self):
        return self.name


class Transport(models.Model):
    code_name = models.UUIDField(default=uuid.uuid4(), unique=True, null=False)
    waybill = models.ForeignKey(to='Waybills', on_delete=models.CASCADE, blank=True, null=True)
    road_time = models.PositiveIntegerField()

    def __str__(self):
        return str(self.code_name)


class Waybills(models.Model):
    start_point = models.ForeignKey(to=Localization, related_name='start_point', on_delete=models.CASCADE)
    end_point = models.ForeignKey(to=Localization, related_name='end_point', on_delete=models.CASCADE)
    max_road_time = models.PositiveIntegerField(null=True)
    list_of_transport = models.ManyToManyField(to=Transport, related_name='transports')

    def __str__(self):
        return f'{self.start_point} - {self.end_point}'