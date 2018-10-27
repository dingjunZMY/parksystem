import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from park1.form import Park1Form
from park1.models import Park1

@method_decorator(csrf_exempt,name='dispatch')
class Park1View(View):
    def post(self,request):
        res=Park1Form(request.POST)
        print(res.is_valid())
        if  not res.is_valid():
            return HttpResponse(status=422)
        park=Park1.objects.create(park_name=res.data.get('park_name'),company_id=res.data.get('company_id'))
        return HttpResponse(status=201)

    def put(self,request,park_id):
        print(park_id)
        stream=request.body.decode()
        json_data=json.loads(stream)
        Park1.objects.filter(park_id=park_id).update(park_name=json_data['park_name'])
        return HttpResponse(status=204)

    def delete(self,request,park_id):
        print(park_id)
        Park1.objects.filter(park_id=park_id).delete()
        return HttpResponse(status=204)

    def get(self,request):
        print(request.GET)
        res=Park1Form(request.GET)
        content=res.data
        #提交参数为停车场ID时按ID查询停车场信息
        if 'park_id' in content.keys():
            if not res.is_valid():
                return HttpResponse(status=422)
            park1=Park1.objects.filter(park_id=content['park_id'])
            return HttpResponse(status=200,content=park1.__str__())
        # 提交参数为停车场名称时按名称查询停车场信息
        elif 'park_name' in content.keys():
            if not res.is_valid():
                return HttpResponse(status=422)
            park1=Park1.objects.filter(park_name=content['park_name'])
            print(park1.__str__())
            return HttpResponse(status=200,content=park1.__str__())
        # 没有提交参数时查询所有停车场信息
        else:
            park1s=Park1.objects.all()
            return HttpResponse(status=200,content=park1s.__str__())




