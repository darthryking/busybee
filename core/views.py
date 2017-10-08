import json

from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import get_object_or_404

from bb_auth.views import AuthView
from core.models import Project, Task, Tag

MAX_PER_PAGE = 25
BAD_REQUEST = HttpResponseBadRequest("Bad Request!")


def coerce_bool(b):
    b = b.lower()
    
    if b in {'true', 'yes', 't', '1'}:
        return True
    elif b in {'false', 'no', 'f', '0'}:
        return False
    else:
        return bool(b)
        
        
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
        
        return HttpResponse(json.dumps(list(projectIds)))
        
    def get_project(self, request, id):
        project = get_object_or_404(Project, id=id, **self.fields)
        projectJson = json.dumps(model_to_dict(project))
        return HttpResponse(projectJson)
        
        
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
        includeComplete = coerce_bool(getData.get('complete', 'true'))
        includeIncomplete = coerce_bool(getData.get('incomplete', 'true'))
        includeInactive = coerce_bool(getData.get('inactive', 'false'))
        
        if tags is None:
            tasks = Task.objects.filter(project__user=request.user)
        else:
            try:
                tagIDs = [int(tagID.strip()) for tagID in tags.split(',')]
            except ValueError:
                return BAD_REQUEST
                
            tasks = Task.objects.filter(
                project__user=request.user,
                tags__id__in=tagIDs,
            )
            
        if project != 'all':
            try:
                tasks = tasks.filter(project__id=int(project))
            except ValueError:
                return BAD_REQUEST
                
        # TODO: Timestamp filtering
        
        if includeComplete and not includeIncomplete:
            tasks = tasks.filter(complete=True)
        elif not includeComplete and includeIncomplete:
            tasks = tasks.filter(complete=False)
        elif not includeComplete and not includeIncomplete:
            return HttpResponse(json.dumps([]))
        else:
            assert includeComplete and includeIncomplete
            
        if not includeInactive:
            tasks = tasks.filter(project__active=True)
            
        tasks = tasks.distinct()
        tasksJson = json.dumps([task.to_dict() for task in tasks])
        
        return HttpResponse(tasksJson)
        
    def get_task(self, request, id):
        task = get_object_or_404(Task, id=id, project__user=request.user)
        taskJson = json.dumps(task.to_dict())
        return HttpResponse(taskJson)
        
        