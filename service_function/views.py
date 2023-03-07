from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *
from django.views.generic import CreateView, ListView


def index(request):
    if request.method == 'POST':
        form = FindWaybillForm(request.POST)
        start_point = int(request.POST['start_point'])
        end_point = int(request.POST['end_point'])
        waybills = Waybills.objects.filter(start_point=start_point, end_point=end_point).order_by('max_road_time')
        return render(request, 'service_function/index.html', context={'form': form, 'waybills': waybills})
    else:
        form = FindWaybillForm()
    return render(request, 'service_function/index.html', context={'form': form})


class AddLocalizationView(CreateView):
    template_name = 'service_function/add_localization.html'
    form_class = LocalizationCreateForm

    def get_success_url(self):
        success_url = reverse('localizations')
        return success_url


class AllLocalizationsView(ListView):
    template_name = 'service_function/localizations.html'
    model = Localization
    context_object_name = 'localizations'


class AllTransportView(ListView):
    template_name = 'service_function/transports.html'
    model = Transport
    context_object_name = 'transports'


class AddTransportView(CreateView):
    template_name = 'service_function/add_transport.html'
    form_class = TransportCreateForm
    context_object_name = 'transports'

    def get_success_url(self):
        success_url = reverse('transports')
        return success_url

    def post(self, request, *args, **kwargs):
        waybill_id = int(request.POST['waybill'])
        road_time = int(request.POST['road_time'])
        waybill = Waybills.objects.get(id=waybill_id)
        for transport in Transport.objects.all():
            if transport.waybill == waybill and transport.road_time == road_time:
                return HttpResponse('Error please choose another road time')
        return super().post(request, *args, **kwargs)


class AddWaybillView(CreateView):
    template_name = 'service_function/add_waybill.html'
    form_class = WaybillCreateForm

    def get_success_url(self):
        success_url = reverse('waybills')
        return success_url


class WaybillsList(ListView):
    template_name = 'service_function/waybills.html'
    model = Waybills
    context_object_name = 'waybills'
