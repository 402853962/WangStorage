from django.urls import path
from book.views import index,login,book,login_json,header,detail,jsonresponse,to_index
# book,login_json,header,detail,jsonresponse,to_index

urlpatterns = [
    path('index/',index),
    path('login/', login),
    path('<cat_id>/<book_id>/',book),
    path('login_json/', login_json),
    path('header/', header),
    path('detail/', detail),
    path('jsonresponse/', jsonresponse),
    path('to_index/', to_index)
]