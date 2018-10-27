import json

from django.db.models import F
from django.http import HttpResponse


from django.shortcuts import render


# Create your views here.

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


from company.forms import CompanyForm
from company.models import Company

@method_decorator(csrf_exempt,name='dispatch')
class CompanyView(View):
    def post(self,request):
        res=CompanyForm(request.POST)
        if not res.is_valid():
            return HttpResponse(status=422)
        company=Company.objects.create(company_name=res.data.get('company_name'))
        return HttpResponse(status=201,content={'company_id':company.company_id}['company_id'])

    def get(self,request):
        res=CompanyForm(request.GET)
        content=res.data
        #当提交参数为企业ID时就查询该企业下所有的停车场
        if 'company_id' in content.keys():
            if not res.is_valid():
                return HttpResponse(status=422)
            company = Company.objects.get(company_id=content['company_id'])
            park_of_company = company.park1_company.all()
            listp = []
            for _ in park_of_company:
                listp.append(_.__str__())
            return HttpResponse(status=200,content=(listp.__str__()))
        #当提交参数为企业名称时查询该企业的详细信息
        elif 'company_name' in content.keys():
            if not res.is_valid():
                return HttpResponse(status=422)
            company=Company.objects.filter(company_name=content['company_name'])
            return HttpResponse(status=200,content=company.__str__())
        #如果不提交参数查询所有的企业信息
        else:
            companyf=Company.objects.filter(updated_time__gt=F('created_time'))
            companys=Company.objects.all()
            return HttpResponse(status=200,content=(companys.__str__(),companyf.__str__()))

    #通过JSON格式提交请求体，可以根据企业ID修改企业的名称
    def put(self,request,company_id):
        print(company_id)
        stream=request.body.decode()
        json_data=json.loads(stream)
        print(json_data)
        Company.objects.filter(company_id=company_id).update(company_name=json_data['company_name'])
        return HttpResponse(status=204)

    def delete(self, request,company_id):
        Company.objects.filter(company_id=company_id).delete()
        return HttpResponse(status=204)




