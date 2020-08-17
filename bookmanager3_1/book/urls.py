from django.urls import path
from book.views import index,book,login,login_json,header

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',book),
    path('login/',login),
    path('login_json/',login_json),
    path('header/',header),
]