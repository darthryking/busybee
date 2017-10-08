from django.db import transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

from bb_auth.models import UserProfile
from bb_auth.forms import RegisterForm


class AuthView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
        
class RegisterPage(View):
    template_name = 'auth/register.html'
    
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('ui_index')
            
        context = {
            'form' : RegisterForm(),
        }
        
        return render(request, self.template_name, context)
        
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            with transaction.atomic():
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password1'],
                )
                
                userProfile = UserProfile(
                    user=user,
                    timezone=data['timezone'],
                )
                userProfile.save()
                
                login(
                    request,
                    authenticate(
                        username=user.username,
                        password=data['password1'],
                    )
                )
                
            return redirect('ui_index')
            
        else:
            context = {
                'form' : form,
            }
            
            return render(request, self.template_name, context)
            
            