# Django_ip

###  统计访问各个接口以及页面的ip及其来自的国家地区

##### 1.工程总体设计
&emsp; 本工程主要为测试性工程，主要涉及到四个页面，ip.html、moban.html、post.html以及search-form页面，ip页面主要展示数据库中内容，模板页面为模板语言的使用和演示，post以及search页面为学习Django对表单处理的最简单基本的get以及post方式。

##### 2工程详细
###### 2.1数据库设计
&emsp; 使用mysql数据库，库名称为django，
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'Django',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
&emsp; 具体的表结构为，其中test为数据库测试表，尝试增删改查等基本操作，Useip为访问用户的信息主要包括用户ip以及ip来自地区，VisitNumber为根据用户访问ip地区做出的统计，包含访问次数以及访问地区，三张表都包含默认字段id
```python

class Test(models.Model):
    name = models.CharField(max_length=20)


class Userip(models.Model):
    ip=models.CharField(max_length=30)
    area =models.CharField(max_length=100)
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip
class VisitNumber(models.Model):
    count = models.IntegerField(default=0)
    area=models.CharField(max_length=100) #网站访问总次数
    class Meta:
        verbose_name = '网站访问统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)
```
###### 2.2hello页面设计
&emsp; 主要为一些模板语言测试
```python
{#单独字符串#}
{{ a }}

{#类的对象。通过 点属性 可以获取属性值#}
{{ template.name }}

{#字典类型的 直接取key对应的value#}
{{ dic.name }}


.......
```
&emsp; 传参业务逻辑为
```python
return render(request, 'moban.html', {'template': p1,
                                             'a': s,
                                             'l': l,
                                             'dic': dic,
                                             'ss': ss,
                                             'list_dic': list_dic,
                                             'file_size': file_size,
                                             'date': datetime.datetime.now()})
```
![Image text](https://github.com/T00youngT00simple/Django_ip/raw/master/img/hello.png)
###### 2.3search_form以及post页面设计
&emsp; 主要为Django处理表单时的get以及post操作
```html
......
        <input type="text" name="q">
        <input type="submit" value="Submit">
......
```
&emsp;业务逻辑
```python
def index(request):
    return render(request,'search_form.html')
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        messsage = 'what do you need is :' + request.GET['q']
    else:
        messsage = 'empty'
    return HttpResponse(request.GET)
def search_post(request):
    client_ip, area = change_info.change_info(request)
    updateDB.updateDB(request, area, client_ip)
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request,'post.html',ctx)
```

![Image text](https://github.com/T00youngT00simple/Django_ip/raw/master/img/get.png)
![Image text](https://github.com/T00youngT00simple/Django_ip/raw/master/img/post.png)
###### 2.4访问ip以及归属地区的获取
2.4.1访问ip的获得
&emsp;可有request.META中的HTTP_X_FORWARDED_FOR字段获得，得到用户访问ip后，可通过藉由requests库对免费接口http://ip.taobao.com/service/getIpInfo.php?ip= 发出请求，对返回的json进行解析后可获得访问ip的国家及地区，这系列逻辑在change_info,py文件中完成
```python
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
```

2.4.2数据库操作
&emsp;针对访问ip以及地区做入库操作Userip，若访问地区第一次出现在VisitNumber中，做插入操作，count为1、不是第一次则将想对应字段count自加一。在文件uodateDB.py中完成。
```python
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
```
2.4.3访问设置
&emsp;在每个页面访问的业务逻辑中调用获取ip，地区函数以及更新数据库函数可实现记录对每个页面访问ip的信息统计
```python
	  client_ip, area = change_info.change_info(request)
    updateDB.updateDB(request, area, client_ip)
```
###### 2.4ip页面
&emsp;ip页面主要展示数据库中内容，没有过多的样式
```html
......
    <h1>ip访问信息</h1>
    <table>
    <tr>
        <th>ip地址</th>
        <th>访问地区</th>
    </tr>
    {% for line in ip_list %}
    <tr>
        <td>{{line.ip}}</td>
        <td>{{line.area}}</td>
    </tr>
    {% endfor %}
    </table>


    <h1>ip统计</h1>
    <table>
    <tr>
        <th>次数</th>
        <th>访问地区</th>
    </tr>
    {% for line in tongji_list %}
    <tr>
        <td>{{line.count}}</td>
        <td>{{line.area}}</td>
    </tr>
    {% endfor %}
.....

```

```python
    ip_list = Userip.objects.all()
    tongji_list = VisitNumber.objects.all()
    return render(request, 'ip.html', {"ip_list":ip_list,"tongji_list":tongji_list})
```

![Image text](https://github.com/T00youngT00simple/Django_ip/raw/master/img/ipshow.png)
