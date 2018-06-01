from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .models import Website 
from .forms import UserForm

# Create your views here.
def index(request):
    latest_websites = Website.objects.all()
    context = {
        'latest_websites': latest_websites,
    }
    return render(request, 'passwordsecure/index.html', context)
    
def detail(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    return render(request, 'passwordsecure/detail.html', {'website': website})
    
class WebsiteCreate(CreateView):
    model = Website
    fields = ['site_name','email','password','notes']
    
    
class WebsiteUpdate(UpdateView):
    model = Website
    fields = ['site_name']
    
class WebsiteDelete(DeleteView):
    model = Website
    success_url = reverse_lazy('passwordsecure:index')
    
# class EmailCreate(CreateView):
#     model = Email
#     fields = ['username','password']
    
# class EmailUpdate(UpdateView):
#     model = Email
#     fields = ['username','password']
    
# class EmailDelete(DeleteView):
#     model = Email
#     success_url = reverse_lazy('passwordsecure:detail')
    
    
  
    
    
    
    # User Registration
class UserFormView(View):
    form_class = UserForm
    template_name = 'passwordsecure/registration_form.html'
    
    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    # Proccess form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        # Further validation
        if form.is_valid():
            
            user = form.save(commit=False)
            
            # cleaned (formatted) data
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # for changing passwords
            user.set_password(password)
            # save user to database
            user.save()
            
            
#             # returns user objects if creditials are correct
#             user = authenticate(username=username,password=password)
            
            
#             # if the user exists in database
#             if user is not None:
                
#                 # checks if user is banned or not
#                 if user.is_active:
#                     login(request,user)
#                     return redirect('passwordsecure:index')
            
#         return render(request, self.template_name, {'form':form})    
            
            
# class login_view(request):
#     if request.method == 'POST':
#         context = {'form':form}
#     else:
#         form = AuthenticationForm()
#     return render(request, 'passwordsecure/login.html', {'form':form})
        
            
        
        
        
        
        
        
        
        
        
        
        