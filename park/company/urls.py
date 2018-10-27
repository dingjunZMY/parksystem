from django.conf.urls import url
from company.views import CompanyView

urlpatterns=[
    url(r'^companies$',CompanyView.as_view()),
    url(r'^companies/(?P<company_id>\w+)/park1s$',CompanyView.as_view())
]