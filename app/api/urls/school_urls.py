from django.conf.urls import url

from api.views.school_views import SchoolView

urlpatterns = [
    url(r'^schools/', SchoolView.as_view(), name = 'schools'),

]