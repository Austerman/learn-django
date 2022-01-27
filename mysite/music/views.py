from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def music_index(request):
    return HttpResponse('music index')