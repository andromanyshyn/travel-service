from django.contrib import admin
from .models import *


@admin.register(Localization)
class LocalizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    pass


@admin.register(Waybills)
class WaybillsAdmin(admin.ModelAdmin):
    pass
