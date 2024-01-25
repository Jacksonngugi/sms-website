from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(contact)
admin.site.register(Message)
admin.site.register(unread_sms)
admin.site.register(chats)
admin.site.register(smscounter)
admin.site.register(sms_count)
