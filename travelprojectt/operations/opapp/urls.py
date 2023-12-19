from.import views
from django.urls import path

urlpatterns=[
    path('',views.demo,name='demo'),
    path('add/',views.addition,name='addition'),
    path('diff/',views.addition,name='difference'),
    path('mul/',views.addition,name='multiplication'),
    path('div/',views.addition,name='division'),


]