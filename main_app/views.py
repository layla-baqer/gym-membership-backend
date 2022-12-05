from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Membership, Class

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
  return HttpResponse('<h1>Home Page</h1>')
#   return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About Page</h1>')

def classes(request):
    return HttpResponse('<h1>Classes</h1>')

def class_detail(request, class_id):
    return HttpResponse('<h1>Class Details</h1>')

def membership(request):
    return HttpResponse('<h1>Member Data</h1>')

class MembershipCreate(CreateView):
    model = Membership
    fields = '__all__'
    success_url=''

class MembershipUpdate(CreateView):
    model = Membership
    fields = ['location']
    success_url=''