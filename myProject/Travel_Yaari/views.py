from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")