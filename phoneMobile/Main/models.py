from django.db import models
from jsonfield import JSONField

def default_specific_workouts():
    return {"posts": []}

class GroupHome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class MainAdmin(models.Model):  
    name = models.CharField(max_length=200)
    group_home = models.ForeignKey(GroupHome, on_delete=models.CASCADE, blank=True, null=True)
    info = JSONField(default = default_specific_workouts())

    def __str__(self):
        if self.group_home is None:
            return self.name
        else:
            return f'{self.group_home}: {self.name}'
