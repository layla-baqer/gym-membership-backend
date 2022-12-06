from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Membership, Class

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def classes(request):
    classes_list = Class.objects.all()

    return render(request, 'classes/index.html', {
        'classes': classes_list
    })

@login_required
def class_detail(request, class_id):
    return HttpResponse('<h1>Class Details</h1>')

@login_required
def assoc_class(request, membership_id, class_id):
  Membership.objects.get(user_id=membership_id).classes.add(class_id)
  return redirect('membership', user_id=membership_id)

@login_required
def membership(request, user_id):
    try:
        classes_list = Membership.objects.get(user_id=user_id).classes.all()
        membership = Membership.objects.get(user_id=user_id)
        return render(request, 'membership/index.html', {
            'membership': membership,
            'classes': classes_list
            })
    except:
        return redirect('membership_create')

class MembershipCreate(CreateView):
    model = Membership
    fields = ['location', 'start_date', 'end_date', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url='/home'

class MembershipUpdate(CreateView):
    model = Membership
    fields = ['location']
    success_url=''


############################
# signup

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)