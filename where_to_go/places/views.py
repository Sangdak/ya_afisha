from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def start_page(request):
    return render(request, 'index.html')
