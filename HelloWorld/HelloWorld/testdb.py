from django.http import HttpResponse
from TestModel.models import Test
def testdb(request):


    #
    # response = ''
    # response1 = ''
    #
    #
    #
    # list = Test.objects.all()     #select* from
    #
    # response2 = Test.objects.filter(id = 1 )  #select *from where 过滤器
    #
    # response3 = Test.objects.get(id = 1)     #获得单个对象
    #
    # response4 = Test.objects.order_by("name")[0:2]   #sql  offset
    #
    # Test.objects.order_by("id")       #id排序
    #
    # Test.objects.filter(name ='runoob').order_by("id")
    #
    #
    # for var in list:
    #     response1 += var.name +""

    # response = response1


    # test1 = Test.objects.filter(id=1)
    # test1.name = 'Goole'
    # test1.save()

    tess1 = Test.objects.get(id =1)
    tess1.delete()


    return HttpResponse('删除成功')


