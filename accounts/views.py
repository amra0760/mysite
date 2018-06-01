from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    
    )
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserLoginForm
from .models import Website 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View


def index(request):
    latest_websites = Website.objects.all()
    context = {
        'latest_websites': latest_websites,
    }
    return render(request, 'accounts/index.html', context)

def detail(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    return render(request, 'acounts/detail.html', {'website': website})

# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)      
        if user is not None:
          login(request, user)
          # or any other success page
        #   return HttpResponse("Logged in")
          return HttpResponseRedirect('accounts/index.html')
    return render(request, "accounts/form.html", {"form":form, "title": title})
    
class WebsiteCreate(CreateView):
    model = Website
    fields = ['site_name']
    
class WebsiteUpdate(UpdateView):
    model = Website
    fields = ['site_name']
    
class WebsiteDelete(DeleteView):
    model = Website
    success_url = reverse_lazy('accounts:index')    
 
    
    
    
    
    
    
    
# def register_view(request):
#     return render(request,"accounts/form.html",{})
    
# def logout_view(request):
#     return render(request,"accounts/form.html",{})
    
    
    
    
    
    
    
    
    
    
    