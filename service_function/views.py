import uuid

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from .models import *


def index(request):
    if request.method == 'POST':
        form = FindWaybillForm(request.POST)
        # if 'name' not in request.POST:
        start_point = int(request.POST['start_point'])
        end_point = int(request.POST['end_point'])
        max_road_time = int(request.POST['max_road_time'])
        waybills = Waybills.objects.filter(start_point=start_point, end_point=end_point,
                                           max_road_time__lte=max_road_time).order_by('max_road_time')
        waybill_start_end_points = Waybills.objects.filter(start_point=start_point, end_point=end_point)
        if not waybill_start_end_points:
            messages.error(request, 'There is no waybill satisfying the search')
            return redirect(reverse('index'))
        if waybills:
            return render(request, 'service_function/index.html',
                          context={'form': form, 'waybills': waybills, 'form2': SaveWaybillForm(request.POST)})
        else:
            messages.error(request, 'The travel time is longer than the one you selected. Change the time')
        # elif 'name' in request.POST:
        #     name = request.POST['name']
        #     SavedWaybills.objects.create(name=name)
        #     return redirect(reverse('index'))
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


def AddTransport(request):
    if request.method == 'POST':
        waybill_id = int(request.POST['waybill'])
        road_time = int(request.POST['road_time'])
        code_name = str(request.POST['code_name'])
        waybill = Waybills.objects.get(id=waybill_id)
        for transport in Transport.objects.all():
            if transport.waybill == waybill and transport.road_time == road_time:
                messages.error(request,
                               'Transport with this waybill and road time already exists.Please choose different time in road')
                form = TransportCreateForm(initial={'code_name': uuid.uuid4()})
                return render(request, 'service_function/add_transport.html', context={'form': form})
        Transport.objects.create(code_name=code_name, waybill=waybill, road_time=road_time)
        return render(request, 'service_function/transports.html', context={'transports': Transport.objects.all()})
    else:
        form = TransportCreateForm(initial={'code_name': uuid.uuid4()})
    return render(request, 'service_function/add_transport.html', context={'form': form})


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


class AllSavedWaybillsList(ListView):
    template_name = 'service_function/saved_waybills.html'
    model = SavedWaybills
    context_object_name = 'savedwaybills'


def delete_localization(request, id_localization):
    localization = Localization.objects.get(id=id_localization)
    localization.delete()
    return redirect(request.META['HTTP_REFERER'])


def delete_transport(request, id_transport):
    transport = Transport.objects.get(id=id_transport)
    transport.delete()
    return redirect(request.META['HTTP_REFERER'])