from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Beast

# Create your views here.
class BeastUpdate(UpdateView):
    model = Beast
    fields = ['breed', 'description', 'magic_abilities', 'dangers', 'habitat', 'age']

class BeastDelete(DeleteView):
    model = Beast
    success_url = '/beasts/'

class BeastCreate(CreateView):
    model = Beast
    fields = '__all__'
    success_url = '/beasts/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beasts_index(request):
    beasts = Beast.objects.all()
    return render(request, 'beasts/index.html', { 'beasts': beasts })

def beasts_detail(request, beast_id):
    beast = Beast.objects.get(id=beast_id)
    return render(request, 'beasts/detail.html', { 'beast': beast} )