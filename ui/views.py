from django.shortcuts import render
from django.views.generic import TemplateView

from bb_auth.views import AuthView


class TemplateAuthView(AuthView, TemplateView):
    pass
    
    
class IndexPage(TemplateView):
    template_name = 'index.html'
    
    
class DashboardPage(TemplateAuthView):
    template_name = 'ui/dashboard.html'
    
    
class ProjectPage(TemplateAuthView):
    template_name = 'ui/project.html'
    
    
class TagsPage(TemplateAuthView):
    template_name = 'ui/tags.html'
    
    