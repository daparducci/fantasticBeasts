from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Beast, Toy, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'kittencollection'

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
    toys_beast_doesnt_have = Toy.objects.exclude(id__in = beast.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'beasts/detail.html', { 'beast': beast, 'feeding_form': feeding_form, 'toys': toys_beast_doesnt_have 
    })

def add_feeding(request, beast_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.beast_id = beast_id
        new_feeding.save()
    return redirect('detail', beast_id=beast_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, beast_id, toy_id):
  Beast.objects.get(id=beast_id).toys.add(toy_id)
  return redirect('detail', beast_id=beast_id)

def toy_remove(request, beast_id, toy_id):
  Beast.objects.get(id=beast_id).toys.remove(toy_id)
  return redirect('detail', beast_id=beast_id)

def add_photo(request, beast_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # session = boto3.Session(profile_name="beastslab")
    # s3 = session.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, beast_id=beast_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', beast_id=beast_id)