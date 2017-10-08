import json
import logging
from datetime import datetime

from django.utils import dateparse, timezone
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import get_object_or_404

from bb_auth.views import AuthView
from core.models import Project, Task, Tag

LOGGER = logging.getLogger(__name__)

MAX_PER_PAGE = 25
BAD_REQUEST = HttpResponseBadRequest(
    json.dumps({'error': "Bad Request!"}),
    content_type='application/json',
)


def bad_request(e=None):
    if e is not None:
        LOGGER.info(
            "Caught exception while handling bad request: %s", e
        )
    return BAD_REQUEST
    
    
def coerce_bool(b):
    lower = b.lower()
    
    if lower in {'true', 'yes', 't', '1', '9001', 'uh-huh', 'k', 'sure'}:
        return True
    elif lower in {'false', 'no', 'f', '0', 'nuh-uh!', '-1', 'stop that'}:
        return False
    else:
        raise ValueError(b)
        
        
class JsonResponse(HttpResponse):
    def __init__(self, *args, content_type='application/json', **kwargs):
        super().__init__(*args, content_type=content_type, **kwargs)
        
        
class ProjectsView(AuthView):
    def get(self, request, id=None):
        if id is None:
            return self.get_project_ids(request)
        else:
            return self.get_project(request, int(id))
            
    def get_project_ids(self, request):
        ''' Retrieve a list of all Project IDs for this User. '''
        
        projectIds = (
            Project.objects
                .filter(user=request.user)
                .values_list('id', flat=True)
        )
        
        return JsonResponse(json.dumps(list(projectIds)))
        
    def get_project(self, request, id):
        project = get_object_or_404(Project, id=id, user=request.user)
        projectJson = json.dumps(project.to_dict())
        return JsonResponse(projectJson)
        
        
class TasksView(AuthView):
    Model = Task
    
    def get(self, request, id=None):
        if id is None:
            return self.get_constrained_tasks(request)
        else:
            return self.get_task(request, int(id))
            
    def get_constrained_tasks(self, request):
        ''' Retrieve a constrained list of tasks for this User. '''
        
        getData = request.GET
        
        tags = getData.get('tags', None)
        project = getData.get('project', 'all')
        beforeDate = getData.get('before', None)
        afterDate = getData.get('after', None)
        
        try:
            includeComplete = coerce_bool(getData.get('complete', 'true'))
            includeIncomplete = coerce_bool(getData.get('incomplete', 'true'))
            includeInactive = coerce_bool(getData.get('inactive', 'false'))
        except ValueError as e:
            return bad_request(e)
            
        if tags is None:
            tasks = Task.objects.filter(project__user=request.user)
        else:
            try:
                tagIDs = [int(tagID.strip()) for tagID in tags.split(',')]
            except ValueError as e:
                return bad_request(e)
            else:
                tasks = Task.objects.filter(
                    project__user=request.user,
                    tags__id__in=tagIDs,
                )
                
        if project != 'all':
            try:
                tasks = tasks.filter(project__id=int(project))
            except ValueError as e:
                return bad_request(e)
                
        if beforeDate is not None:
            try:
                beforeDate = self._parse_datestamp(beforeDate)
            except Exception as e:
                return bad_request(e)
            else:
                tasks = tasks.filter(due_time__lt=beforeDate)
                
        if afterDate is not None:
            try:
                afterDate = self._parse_datestamp(afterDate)
            except Exception as e:
                return bad_request(e)
            else:
                tasks = tasks.filter(due_time__gt=afterDate)
                
        if includeComplete and not includeIncomplete:
            tasks = tasks.filter(complete=True)
        elif not includeComplete and includeIncomplete:
            tasks = tasks.filter(complete=False)
        elif not includeComplete and not includeIncomplete:
            return JsonResponse(json.dumps([]))
        else:
            assert includeComplete and includeIncomplete
            
        if not includeInactive:
            tasks = tasks.filter(project__active=True)
            
        tasks = tasks.distinct()
        tasksJson = json.dumps([task.to_dict() for task in tasks])
        
        return JsonResponse(tasksJson)
        
    def get_task(self, request, id):
        task = get_object_or_404(Task, id=id, project__user=request.user)
        taskJson = json.dumps(task.to_dict())
        return JsonResponse(taskJson)
        
    def _parse_datestamp(self, dateStamp):
        try:
            date = dateparse.parse_date(dateStamp)
        except ValueError as e:
            raise
            
        if date is None:
            raise Exception("Malformed datestamp!")
            
        date = datetime.combine(date, datetime.min.time())
        
        try:
            return timezone.make_aware(date)
        except Exception as e:
            raise
            
            