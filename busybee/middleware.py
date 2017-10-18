import logging

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.forms import AuthenticationForm

LOGGER = logging.getLogger(__name__)


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            user = request.user
        except AttributeError:
            return None
            
        if user.is_authenticated():
            timezone.activate(user.userprofile.timezone)
            LOGGER.info("Activate timezone: %s", user.userprofile.timezone)
        else:
            timezone.deactivate()
            
        return None
        
        
def login_form(request):
    return {'login_form': AuthenticationForm()}
    
    