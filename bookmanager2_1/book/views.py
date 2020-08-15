from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse('ok')

from book.models import BookInfo,PeopleInfo

book1 = BookInfo(
    name = '外来生物',
    pub_date = '2020-8-15',
    readcount = '30'
)
book1.save()
book1

PeopleInfo.objects.create(
    name='猴子救兵',
    gender='1',
    description='生猴子',
    book_id='5'
)

book2 = BookInfo.objects.get(id='6')
book2.name='外来物种2'
book2.save()

BookInfo.objects.filter(id='7').update(name='外来物种3')

book3 = BookInfo.objects.get(id='9')
book3.delete()
book3.save()

BookInfo.objects.filter(id='10').delete()

PeopleInfo.objects.all()

PeopleInfo.objects.count()

PeopleInfo.objects.filter(name__contains='黄')

PeopleInfo.objects.filter(name__endswith='冲')

PeopleInfo.objects.filter(id__in=(1,2,3,4))

BookInfo.objects.exclude(id__gt='2')

from django.db.models import F,Q
BookInfo.objects.filter(readcount__gt= F('commentcount'))

BookInfo.objects.filter(Q(readcount__lte='30')|Q(id__gt='2'))

BookInfo.objects.filter(~Q(id=3))

from django.db.models import Sum,Avg,Max

BookInfo.objects.aggregate(Sum('commentcount'))

BookInfo.objects.aggregate(Max('id'))

BookInfo.objects.all().order_by('commentcount')

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

person = PeopleInfo.objects.get(id=1)
person.book.name
person.book.commentcount