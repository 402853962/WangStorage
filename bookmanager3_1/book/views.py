from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def index(request):
    return HttpResponse('ok')

# def book(request,book_id,cat_id):
#     keyword=request.GET.getlist('keyword')
#
#     return HttpResponse(keyword)
#
# def login(request):
#     print(request.POST)
#     return HttpResponse('login')
#
# def login_json(request):
#     body = request.body
#     # print(body)
#     body_str = body.decode()
#     # print(body_str)
#     body_dict = json.loads(body_str)
#     print(body_dict)
#     return HttpResponse('json')
#
# def header(request):
#
#     print(request.META)
#     return HttpResponse('header')
#
# def detail(request):
#     return HttpResponse(content='内容',content_type='text/html',status=200)
#
# from django.http import JsonResponse
# def jsonresponse(request):
#
#     userinfo = {
#         'user_id' : 111,
#         'username' : 'itcast'
#     }
#
#
#     return JsonResponse(userinfo)
#
#
# from django.shortcuts import redirect
# def to_index(request):
#     return redirect('http://www.baidu.com')
#

# def login(request):
#     print(request.POST)
#     return HttpResponse('login')
#
# def book(request,cat_id,book_id):
#     keyword = request.GET.getlist('keyword')
#     print(request.GET)
#     return HttpResponse(keyword)
#
#
# import json
# def login_json(request):
#     body = request.body
#     body_str = body.decode()
#     body_dict = json.loads(body_str)
#     print(body_dict)
#     return HttpResponse('json')
#
# def header(request):
#     if request.method == 'GET':
#         print('GET')
#     elif request.method == 'POST':
#         print('POST')
#     else:
#         print(request.method)
#
#
#     return HttpResponse('header')
#
#
# def detail(request):
#     result = HttpResponse(content='detail',content_type='text/html',status=200)
#     result['name'] = 'jack'
#     return result
#
#
# from django.http import JsonResponse
# def jsonresponse(request):
#     userinfo = {
#         'name' : 'jack',
#         'password' : 123456
#     }
#
#     return JsonResponse(userinfo)
#
# from django.shortcuts import redirect
# def to_index(request):
#     return redirect("http://www.baidu.com/")

def login(request):
    print(request.POST)
    return HttpResponse('login')

def book(request,cat_id,book_id):
    keyword = request.GET.getlist('keyword')
    return HttpResponse(keyword)

import json
def login_json(request):
    body = request.body
    body_str = body.decode()
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse('json')

def header(request):
    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
    else:
        print(request.method)
    head = request.META
    print(head)
    return HttpResponse('header')

def detail(request):
    result = HttpResponse(content='detail',content_type='text/http',status=200)
    result['name'] = 'jack'
    return result

from django.http import JsonResponse
def jsonresponse(request):
    info = {
        'name' : 'jack',
        'password' : 123456
    }
    return JsonResponse(info)

from django.shortcuts import redirect
def to_index(request):
    return redirect('http://www.qq.com')






from book.models import BookInfo,PeopleInfo
from django.core.paginator import Paginator

BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__readcount__gt='30')
# people = PeopleInfo.objects.all()[0:9]
# paginator = Paginator(people,2)
# page_people = paginator.page(2)