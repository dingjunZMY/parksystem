from django.conf.urls import url

from company.views import CompanyView
from park1.views import Park1View

urlpatterns=[
    url(r'^park1s$', Park1View.as_view()),
    url(r'^park1s/(?P<park_id>\w+)$',Park1View.as_view())
]


