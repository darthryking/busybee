import logging

from django.utils import timezone
from django.shortcuts import render
from django.views.generic import View, TemplateView

from bb_auth.views import AuthView

LOGGER = logging.getLogger(__name__)


class TemplateAuthView(AuthView, TemplateView):
    pass
    
    
class IndexPage(View):
    template_name = 'index.html'
    
    def get(self, request):
        context = {
            'time' : timezone.now(),
        }
        LOGGER.info("hi")
        return render(request, self.template_name, context)
    
    
class DashboardPage(TemplateAuthView):
    template_name = 'ui/dashboard.html'
    
    
class ProjectPage(TemplateAuthView):
    template_name = 'ui/project.html'
    
    
class TagsPage(TemplateAuthView):
    template_name = 'ui/tags.html'
    
    