from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def index(requeset):
    return render(requeset,'book/book.html')