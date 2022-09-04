from django.db import models
from jsonfield import JSONField

def default_specific_workouts():
    return {"posts": []}
    
class MainAdmin(models.Model):
    name = models.CharField(max_length=200)
    info = JSONField(default = default_specific_workouts())



    def __str__(self):
        return self.name
