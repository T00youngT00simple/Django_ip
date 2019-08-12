from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
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
