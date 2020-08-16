from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo,PeopleInfo

# Create your views here.
def index(request):
    return HttpResponse('ok')

BookInfo.objects.get(id=1)

BookInfo.objects.create(
    name='外来生物',
    pub_date='2020-8-16',
    readcount='30',
    commentcount='20'
)

BookInfo.objects.get(name='外来生物')


PeopleInfo.objects.create(
    name='猪皮恶霸',
    gender=1,
    description= '肉蛋葱鸡',
    book_id = 5
)

PeopleInfo.objects.filter(name='猪皮恶霸').update(gender=0)

PeopleInfo.objects.filter(name='猪皮恶霸').delete()

BookInfo.objects.filter(name='外来生物').delete()

BookInfo.objects.get(id=1)
BookInfo.objects.filter(name__contains='湖')
BookInfo.objects.filter(name__endswith='部')
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(id__in=(1,3,5))
BookInfo.objects.filter(id__gt=3)
BookInfo.objects.filter(pub_date__year='1980')
BookInfo.objects.filter(pub_date__gt='1990-1-1')

from django.db.models import F,Q

BookInfo.objects.filter(readcount__gte=F('commentcount'))
BookInfo.objects.filter(readcount__gt=20).filter(id__gt=3)
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.filter(~Q(id=3))

from django.db.models import Avg,Sum

BookInfo.objects.aggregate(Avg('readcount'))
BookInfo.objects.aggregate(Sum('commentcount'))
BookInfo.objects.all().order_by('id')
BookInfo.objects.all().order_by('-id')

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

people = PeopleInfo.objects.get(id=1)
people.book.name