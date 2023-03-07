from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse('<marquee><h1>hi deva how r u !!</h1></marquee>')

def d(request):

    return HttpResponse('<marquee>hi bro !!</marquee>')