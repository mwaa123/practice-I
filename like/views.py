from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    
    return render(request,'fold/welcome.html')
