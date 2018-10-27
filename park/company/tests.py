from django.test import TestCase
from company.models import Company
# Create your tests here.
class CompanyTestView(TestCase):
    def setUp(self):
        super(CompanyTestView, self).setUp(())
        Company.objects.create(company_name="ZMY")
        Company.objects.create(company_name="ZMY1")
        Company.objects.create(company_name="ZMY2")
        Company.objects.create(company_name="ZMY3")
        Company.objects.create(company_name="ZMY4")

    def test_CompanyView_get_noparm(self):
        response=self.client.get('/companies')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code,200)