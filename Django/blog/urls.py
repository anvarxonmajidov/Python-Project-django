from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.register, name='signUp'),
    path('user_login/', views.user_login, name='user_login'),
    path('check_user/', views.check_user, name='check_user'),
    path('custom_dashboard/', views.custom_dashboard, name='custom_dashboard'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_product/', views.add_product, name='add_product'),
    path('my_products/', views.my_products, name='my_products'),
    path('single_product/',views.single_product,name='single_product'),
    path('update_product/',views.update_product,name='update_product'),
    path('delete_product/',views.delete_product,name='delete_product'),
    path('allProducts/', views.allProducts, name='allProducts'),
    path('sendEmail/', views.sendEmail, name='sendEmail'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
