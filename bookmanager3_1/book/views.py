from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('ok')

def book(request,book_id,cat_id):
    keyword=request.GET.getlist('keyword')

    return HttpResponse(keyword)

def login(request):
    print(request.POST)
    return HttpResponse('login')













from book.models import BookInfo,PeopleInfo

BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__readcount__gt='30')