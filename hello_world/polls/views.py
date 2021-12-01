import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index_old(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def index(request):
    responseData = {
        'text': 'Hello world, you\'re at the polls index',
    }
    return JsonResponse(responseData)