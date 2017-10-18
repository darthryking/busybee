from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "{}'s project '{}'".format(self.user.username, self.name)
        
    def to_dict(self):
        return model_to_dict(self)
        
        
class Tag(models.Model):
    name =  models.CharField(max_length=256)
    color = models.CharField(max_length=6)
    
    def __str__(self):
        return "Tag '{}'".format(self.name)
        
    def to_dict(self):
        return model_to_dict(self)
        
        
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    due_time = models.DateTimeField(blank=True, null=True)
    
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return "Task for project '{}': {}".format(self.project.name, self.name)
        
    def to_dict(self):
        result = model_to_dict(self, exclude=['tags'])
        result['tags'] = [tag.to_dict() for tag in self.tags.all()]
        return result
        
        