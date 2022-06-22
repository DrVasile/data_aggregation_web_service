"""
data_aggregation_service URL Configuration
"""
from location_data.views import LocationDataCreateView, LocationDataListView, LocationDataUpdateView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", LocationDataListView.as_view(), name="location_data_list"),
    path("create/", LocationDataCreateView.as_view(), name="location_data_create"),
    path("<int:pk>/update/", LocationDataUpdateView.as_view(), name="location_data_update"),
    path("admin/", admin.site.urls)
]
