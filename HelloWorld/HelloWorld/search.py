from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import change_info
from . import updateDB

def index(request):
    client_ip ,area = change_info.change_info(request)
    updateDB.updateDB(request,area,client_ip)
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