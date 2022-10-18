from django.urls import path
from .views import index,contact,about,postDetails,post

urlpatterns=[
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('post/<int:pk>/',postDetails,name='post_detail'),
]
