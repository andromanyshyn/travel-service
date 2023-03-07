from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_localization/', views.AddLocalizationView.as_view(), name='add_localization'),
    path('add_transport/', views.AddTransportView.as_view(), name='add_transport'),
    path('add_waybill/', views.AddWaybillView.as_view(), name='add_waybill'),

    path('localizations/', views.AllLocalizationsView.as_view(), name='localizations'),
    path('transports/', views.AllTransportView.as_view(), name='transports'),
    path('waybills/', views.WaybillsList.as_view(), name='waybills'),
]
