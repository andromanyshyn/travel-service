from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_localization/', views.AddLocalizationView.as_view(), name='add_localization'),
    path('add_transport/', views.AddTransport, name='add_transport'),
    path('add_waybill/', views.AddWaybillView.as_view(), name='add_waybill'),

    path('localizations/', views.AllLocalizationsView.as_view(), name='localizations'),
    path('transports/', views.AllTransportView.as_view(), name='transports'),
    path('waybills/', views.WaybillsList.as_view(), name='waybills'),
    path('saved_waybills/', views.AllSavedWaybillsList.as_view(), name='saved_waybills'),

    path('localization/delete/<int:id_localization>', views.delete_localization, name='delete_localization'),
    path('transport/delete/<int:id_transport>', views.delete_transport, name='delete_transport'),
]