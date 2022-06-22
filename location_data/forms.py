from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from location_data.models import LocationData


class LocationDataForm(forms.ModelForm):

    class Meta:
        model = LocationData
        fields = ("object_id", "latitude", "longitude")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Location Data"))
