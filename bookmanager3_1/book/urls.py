from django.urls import path
from book.views import index
from book import views
from django.urls import converters
# book,login_json,header,detail,jsonresponse,to_index

######################################
# class MobileConverter:
#     regex='1[3-9]\d{9}'
#
#     def to_python(self,value):
#         return value
#
# converters.register_converter(MobileConverter,'mobile')
######################################
######################################
class MobileConverter:
    regex='1[3-9]\d{9}'

    def to_python(self,value):
        return value

converters.register_converter(MobileConverter,'mobile')
######################################

urlpatterns = [
    path('index/',index),
    # path('login/', login),
    # path('<cat_id>/<book_id>/',book),
    # path('login_json/', login_json),
    # path('header/', header),
    # path('detail/', detail),
    # path('jsonresponse/', jsonresponse),
    # path('to_index/', to_index),
    path('p/<int:tieba_id>/', views.baidu_tieba),
    path('register/<mobile:phone>/', views.tieba_register),
    path('tieba_login/', views.tieba_login),
    path('get_cookies/', views.get_cookies),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session),
    path('jd_register/', views.jd_register),

    path('meiduo_register/',views.RegisterView.as_view()),
    path('center/',views.CenterView.as_view())
]