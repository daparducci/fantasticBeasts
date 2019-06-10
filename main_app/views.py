class Beast:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

beasts = [
    Beast('Lolo', 'tabby', 'foul little demon', 3),
    Beast('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Beast('Raven', 'black tripod', '3 legged cat', 4)
]

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> Hi Hi Home </h1>')

def about(request):
    return render(request, 'about.html')

def beasts_index(request):
    return render(request, 'beasts/index.html', { 'beasts': beasts })