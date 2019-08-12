from TestModel.models import *
from django.utils import timezone
import requests
import json

# 自定义的函数，不是视图
def change_info(request):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='


    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip

    req = requests.get(url + client_ip)

    html = req.content.decode('utf-8')
    html = json.loads(html)

    if html['data']['city'] == '内网IP':
        area = '内网IP'
    else:
        area = html['data']['country']+html['data']['region']+html['data']['city']


    return client_ip,area

