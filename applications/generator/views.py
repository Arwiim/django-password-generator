#Python Imports
import random
import string
#Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def home(request):
    return render(request,'generator/home.html', {'password':'hui43g6iu3o4'})

def about(request):
    return render(request,'generator/about.html')

def password(request):
    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('`,~,!,@,#,%,$,^,&,*,(,),_,-,+,=,{,[,},},|,\,:,;,'))
    if request.GET.get('numbers'):
        characters.extend(list('0,1,2,3,4,5,6,7,8,9'))

    if request.GET.get('length'):
        length = int(request.GET.get('length',))
    else:
        length = 12
    
    thepassword = ''

    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})


