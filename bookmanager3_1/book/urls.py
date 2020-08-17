from django.urls import path
from book.views import index,book,login

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',book),
    path('login/',login)
]