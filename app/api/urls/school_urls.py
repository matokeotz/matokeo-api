from django.conf.urls import url

from api.views.school_views import SchoolView, SchoolStatisticsView

urlpatterns = [
    url(r'^school/(?P<school>[a-zA-Z-]+)/years/', SchoolStatisticsView.as_view(), name='schoolstatistics'),
    url(r'^schools/', SchoolView.as_view(), name='schools'),

]