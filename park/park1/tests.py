from django.test import TestCase

# Create your tests here.

from company.models import Company
from park1.models import Park1


class Park1TestView(TestCase):
    def setUp(self):
        super(Park1TestView, self).setUp(())
        Park1.objects.create(park_name="ZMY-parking1")
        Park1.objects.create(park_name="ZMY-parking2")

    def test_Park1View_get_noparm(self):
        response=self.client.get('/park1s')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code,200)

