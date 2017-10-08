from django.shortcuts import render, redirect
from django.views.generic import View

from bb_auth.forms import RegisterForm


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
        return redirect('ui_index')
        
        