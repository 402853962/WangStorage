from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('ok')

from book.models import BookInfo,PeopleInfo

BookInfo.objects.get(id=1)
BookInfo.objects.create(
    name = '外来生物',
    pub_date= '2020-8-15',
    readcount= '20',
    commentcount= '30'
)
BookInfo.objects.filter(name='外来生物').update(name = '外来物种')
PeopleInfo.objects.create(
    name='猪皮恶霸',
    gender=1,
    description='肉蛋葱鸡',
    book_id=5
)

BookInfo.objects.filter(name='外来物种').delete()
PeopleInfo.objects.filter(name='猪皮恶霸').delete()

BookInfo.objects.get(id=1)
BookInfo.objects.filter(name__contains='湖')
BookInfo.objects.filter(name__endswith='部')
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(id__in=(1,3,5))
BookInfo.objects.filter(id__gt=(3))
BookInfo.objects.filter(pub_date__year='1980')
BookInfo.objects.filter(pub_date__gt='1990-1-1')

from django.db.models import Q,F

BookInfo.objects.filter(commentcount__gt=F('readcount'))
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.filter(~Q(id=3))

from django.db.models import Avg
BookInfo.objects.aggregate(Avg('commentcount'))

BookInfo.objects.all().order_by('readcount')

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

people = PeopleInfo.objects.get(id=3)
people.book.name
people.book.pub_date