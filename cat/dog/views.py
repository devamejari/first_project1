from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def muddi(request):
    return HttpResponse('good morning devendra')