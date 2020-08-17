from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('ok')

def book(request,book_id,cat_id):
    keyword=request.GET.getlist('keyword')

    return HttpResponse(keyword)

def login(request):
    print(request.POST)
    return HttpResponse('login')

def login_json(request):
    body = request.body
    # print(body)
    body_str = body.decode()
    # print(body_str)
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse('json')

def header(request):

    print(request.META)
    return HttpResponse('header')











from book.models import BookInfo,PeopleInfo

BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__readcount__gt='30')