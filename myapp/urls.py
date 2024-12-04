# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),  # Route for the home page
    path('servicedetails/', views.servicedetails, name='servicedetails'),  #route for an "services" page
    path('starter/', views.starter, name='starter'), #route for starter page
    path('about/', views.about, name='about'), #route for starter page
    path('doctors/', views.doctors, name='doctors'), #route for starter page
    path('services/', views.services, name='services'), #route for starter page
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('responses/', views.responses, name='responses'),
    path('appointment1/', views.appointment1, name='appointment1'),
    path('contact1/', views.contact1, name='contact1'),
    path('edit/', views.edit, name='edit'),
    path('show/', views.show, name='show'),

    path('delete/<int:id>', views.delete),
    path('delete_contacts/<int:id>', views.delete_contacts),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),

    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
