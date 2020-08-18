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

# def login(request):
#     print(request.POST)
#     return HttpResponse('login')
#
# def book(request,cat_id,book_id):
#     keyword = request.GET.getlist('keyword')
#     return HttpResponse(keyword)
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
#     head = request.META
#     print(head)
#     return HttpResponse('header')
#
# def detail(request):
#     result = HttpResponse(content='detail',content_type='text/http',status=200)
#     result['name'] = 'jack'
#     return result
#
# from django.http import JsonResponse
# def jsonresponse(request):
#     info = {
#         'name' : 'jack',
#         'password' : 123456
#     }
#     return JsonResponse(info)
#
# from django.shortcuts import redirect
# def to_index(request):
#     return redirect('http://www.qq.com')
#





from book.models import BookInfo,PeopleInfo
from django.core.paginator import Paginator

# BookInfo.objects.filter(peopleinfo__name='郭靖')
# BookInfo.objects.filter(peopleinfo__description__contains='八')
# PeopleInfo.objects.filter(book__name='天龙八部')
# PeopleInfo.objects.filter(book__readcount__gt='30')
# people = PeopleInfo.objects.all()[0:9]
# paginator = Paginator(people,2)
# page_people = paginator.page(2)



######################################################################
######################################################################
# def baidu_tieba(request,tieba_id):
#     return HttpResponse(tieba_id)

# def tieba_register(request,phone):
#     return HttpResponse(phone)

# def tieba_login(request):
#     username = request.GET.get('username')
#     result = HttpResponse('set_cookie')
#     result.set_cookie(key='username',value=username,max_age=30)
#     return result

# def get_cookies(request):
#
#     print(request.COOKIES)
#     username = request.COOKIES.get('username')
#     return HttpResponse(username)

# def set_session(request):
#     request.session['user_id'] =15423132312
#     return HttpResponse('set_session')

# def get_session(request):
#     user_id = request.session['user_id']
#     #删除数据
#     request.session.clear()
#     #删除数据以及key
#     request.session.flush()
#     #设置过期时间,None为默认，两周
#     request.session.set_expiry(30)
#     return HttpResponse(user_id)

# def jd_register(request):
#     if request.method == 'GET':
#         print('GET')
#     elif request.method == 'POST':
#         print('POST')
#     else:
#         return HttpResponse('other')
#
#     return HttpResponse('jd_register')

# from django.views import View
# class RegisterView(View):
#     def get(self,request):
#         return HttpResponse('view get')
#     def post(self,request):
#         return  HttpResponse('view post')
#     def other(self,request):
#         pass

# from django.contrib.auth.mixins import LoginRequiredMixin
# class CenterView(LoginRequiredMixin,View):
#     def  get(self,request):
#         return HttpResponse('个人中心 get')
#     def post(self,request):
#         return HttpResponse('个人中心 post')

#######################################################################
#######################################################################

def baidu_tieba(request,tieba_id):
    return HttpResponse('tieba_id')

def tieba_register(request,phone):
    return HttpResponse('phone')

def tieba_login(request):
    username = request.GET.get('username')
    result = HttpResponse('set_cookies')
    result.set_cookie(key='username',value='jack',max_age=60)
    return result

def get_cookies(request):
    username = request.COOKIES.get('username')
    return HttpResponse(username)

def set_session(request):
    request.session['user_id']=123456
    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session['user_id']
    request.session.clear()
    request.session.flush()
    request.session.set_expiry(30)
    return HttpResponse('get_session')

def jd_register(request):
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')
    else:
        return HttpResponse('other')

from django.views import View
class RegisterView(View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')
    def other(self,request):
        pass

from django.contrib.auth.mixins import LoginRequiredMixin
class CenterView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')



