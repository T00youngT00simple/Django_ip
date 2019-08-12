#数据库视图

from django.shortcuts import render
from TestModel.models import *
from django.shortcuts import render
def ip(request):
    ip_list = Userip.objects.all()
    tongji_list = VisitNumber.objects.all()
    return render(request, 'ip.html', {"ip_list":ip_list,"tongji_list":tongji_list})