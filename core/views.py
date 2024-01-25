from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import *
import json
import africastalking


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)

            return redirect('index')
        else:
            messages.info(request,'Invalid credation')

            return redirect('login')

    else:
        return render(request,'pages-login.html')
    
@login_required(login_url='login')
def index (request):
    contacts = contact.objects.all()
    sent = sms_count.objects.get(name = "sent_sms")
    remaining = sms_count.objects.get(name = "remaining_sms")
    context = {
        'no_contacts':len(contacts),
        'sent':sent,
        'remaining' : remaining
    }
    return render(request,"index.html",context)

@login_required(login_url='login')
def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        loc = request.POST.get('location')
        gender = request.POST.get('gender')

        if contact.objects.filter(name=name,phone_number=phone_number).exists():
            messages.info(request,'Contact already exists.')

        else:
            new_contact = contact.objects.create(name=name,phone_number=phone_number,location=loc,gender=gender)
            new_contact.save()

    return render(request,'add_contact.html')

@login_required(login_url='login')
def outgoing_sms(request):

    africastalking.initialize(
    username='username',
    api_key= 'api_key',
    )
    
    sms = africastalking.SMS
    sender = '25855'

    if request.method == 'POST':
        phone_no = request.POST['phone']
        print(phone_no)
        recipients = phone_no.split(',')  
        print(recipients)
        message = request.POST['message']
       
        try:    
            for number in recipients:
                user = contact.objects.get(phone_number=number)
                response = sms.send(message, [number], sender)
                print (response)
                db_Sms = Message.objects.create(user=user,content=message,status='outgoing')

                if chats.objects.filter(user_name=user.name) is None:
                    new_chat_member = chats.objects.create(user_name=user.name)
                    new_chat_member.save()
                db_Sms.save()
                
        
        except Exception as e:
                print (f'We have a problem: {e}')

    return render(request,'send_sms.html')

@login_required(login_url='login')
def Chats(request):
    name = request.GET.get('user') or request.POST.get("user")
   
    # obtain the fields of outgoing_sms from chat save  to db
    if request.method == 'POST':
        content = request.POST.get("content")
        status = request.POST.get("status")
        user = contact.objects.get(name = name)
        save_sms = Message.objects.create(user=user,content=content,status=status)
        save_sms.save()

    if name is not None:
        user_contact = contact.objects.get(name=name)
        user_messages = Message.objects.filter(user=user_contact)
        chat_members = chats.objects.all()
        # chat_member = chats.objects.values_list('user_name')[0]
        # print([chat_member])
        context = {
            'members':chat_members,
            'messages':user_messages,
            'name':name,
        }

    else:
        chat_members = chats.objects.all()
        context = {
            'members':chat_members,
        }
    
    return render(request,'chat.html',context)
