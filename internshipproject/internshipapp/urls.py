from os import path

from . import views
from django.urls import path



urlpatterns = [

   #path('',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    #path('data/',views.data,name='data'),
   # path('p/',views.p,name='p'),
   # path('',views.demo1,name='demo1'),          #passing value to another page
    #path('add/',views.addition,name='addition'), #passing value to another page
    # path('',views.demo2,name="demo2"),
     #path('operation/',views.operation,name='operation')

    #project starting..........................................................................

     path('',views.project,name='project'),


 ]