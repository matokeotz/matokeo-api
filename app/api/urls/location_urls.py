from django.conf.urls import url

from api.views.location_views import RegionView, DistrictView, ZoneView, SchoolLocationView

urlpatterns = [
    url(r'^regions/', RegionView.as_view(), name = 'regions'),
]