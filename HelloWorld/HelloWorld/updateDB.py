from django.http import HttpResponse
from TestModel.models import *
def updateDB(request,area,client_ip):
    useip = Userip(ip=client_ip, area=area)
    useip.save()

    area_exist = VisitNumber.objects.filter(area=str(area))
    if area_exist:  # 判断是否存在该ip
        uobj = area_exist[0]
        uobj.count += 1
    else:
        uobj = VisitNumber()
        uobj.area = area
        uobj.count = 1
    uobj.save()
