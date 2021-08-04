from django.shortcuts import render
from email_subscription.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


# Create your views here.

def subscribe(request):
    sub=forms.Subscribe()
    if request.method=='POST':
        sub=forms.Subscribe(request.POST)
        subject='Welcome to ShamStories'
        message='Hope you are enjoying reading our stories and they are changing your life'
        recepient=str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER,[recepient],fail_silently=False)
        return render(request,'emails/success.html',
            {'recepient':recepient})
    return render(request,'emails/index.html',
            {'form':sub})