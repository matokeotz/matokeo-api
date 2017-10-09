from django.conf.urls import url

from api.views.location_views import RegionView, DistrictView, ZoneView, SchoolLocationView

urlpatterns = [
    url(r'^regions/', RegionView.as_view(), name='regions'),
    url(r'^region/(?P<region>[a-zA-Z-0-9]+)/', SchoolLocationView.as_view(), name='schoollocations'),

]