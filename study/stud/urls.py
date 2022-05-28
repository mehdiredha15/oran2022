from .views import home,detail,achat,general,indexx,oran,update,form,ticket,planning
from django.urls import path
urlpatterns = [


    path('',indexx,name='home'),
    path('home/',home,name='athlet'),
    path('home/<str:pk>',home,name='athlet'),
    #path('detail/<str:pk>',detail,name='detail'),
    path('achat/<str:pk>',achat,name='achat'),
    path('achat/update/<str:pk>',update,name='update'),
    path('oran/',oran,name='oran'),
    path('form/<str:pk>',form,name='form'),
    path('ticket/<str:pk>',ticket,name='ticket'),
    path('planning/',planning,name='planning'),
]
