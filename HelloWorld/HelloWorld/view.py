from django.http import HttpResponse
from django.shortcuts import render

from . import change_info
from . import updateDB


# def hello(request):
#     return HttpResponse("HelloWorld!")




def hello(request):
    client_ip, area = change_info.change_info(request)
    updateDB.updateDB(request, area, client_ip)

    s = '你好'
    l = ['aa', 'bb', 'cc']
    ss = '簌簌衣襟落枣花，村南村北响缫车，牛衣古柳卖黄瓜。酒困路长惟欲睡，日高人渴漫思茶，敲门试问野人家。'
    dic = {'name': '二哥', 'age': 18, }

    class Template(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Template('zzy', 18)
    p2 = Template('zxc', 28)
    list_dic = [p1, p2]
    file_size = 12345
    import datetime
    date = datetime.datetime.now()

    use_dit = {'template': p1,
                                             'a': s,
                                             'l': l,
                                             'dic': dic,
                                             'ss': ss,
                                             'list_dic': list_dic,
                                             'file_size': file_size,
                                             'date': datetime.datetime.now()}

    return render(request, 'moban.html', {'template': p1,
                                             'a': s,
                                             'l': l,
                                             'dic': dic,
                                             'ss': ss,
                                             'list_dic': list_dic,
                                             'file_size': file_size,
                                             'date': datetime.datetime.now()})




