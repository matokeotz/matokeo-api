from django.conf.urls import url

from api.views.school_views import SchoolsView

urlpatterns = [
	url(r'^schools/', SchoolsView.as_view(), name = 'schools'),
]