from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from location_data.forms import LocationDataForm
from location_data.models import LocationData


class LocationDataCreateView(CreateView):
    model = LocationData
    fields = ("object_id", "latitude", "longitude")
    success_url = reverse_lazy("location_data_list")


class LocationDataListView(ListView):
    model = LocationData
    context_object_name = "location_data"


class LocationDataUpdateView(UpdateView):
    model = LocationData
    form_class = LocationDataForm
    template_name = "location_data/locationdata_form.html"
    success_url = reverse_lazy("location_data_list")
