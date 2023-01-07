from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse



def home(request):
  skill=Skill.objects.all()
  exp=Exp.objects.all()
  client=Client.objects.all()
  port=Portfolio.objects.all()
  certi=Certificate.objects.all()
  context={'skill':skill,'exp':exp,'test':client, 'port':port,'certi':certi }
  
  return render(request,'resume/index.html',context ) 

def send(request):
  if request.method == 'POST':
    template=render_to_string('resume/try.html',{'name':request.POST['name'],
    'email':request.POST['email'],
    'message':request.POST['message'],
    })
    print(template)
    email=EmailMessage(
      request.POST['subject'],
      template,
      settings.EMAIL_HOST_USER,
      ['parasy787898@gmail.com']
    )

    email.fail_silently=False
    email.send()
    messages.success(request,"sucess")
    return JsonResponse({"error":False})
