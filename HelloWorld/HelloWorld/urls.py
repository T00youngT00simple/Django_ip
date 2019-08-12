"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url



from django.urls import include,re_path

from . import  view,testdb,search,ip,change_info
import pymongo


urlpatterns = [

    re_path(r'^hello$',view.hello),
    re_path(r'^testdb$',testdb.testdb),
    re_path(r'^search-form$',search.index),
    re_path(r'^search$', search.search),
    re_path(r'^search-post$', search.search_post),
    re_path(r'^ip$', ip.ip),
    #数据库视图处理


]

# urlpatterns = [
#
#     url('hello',view.hello),
#
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
