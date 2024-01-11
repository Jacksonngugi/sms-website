from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('add_contact',views.add_contact,name='add_contact'),
    path('send_sms',views.outgoing_sms,name='send_sms'),
    path('chat',views.Chats,name='chat'),
]