from django.db import models
from jsonfield import JSONField

def default_specific_workouts():
    return {"posts": []}


class People(models.Model):
    name_people = models.CharField(max_length=200, verbose_name="Работник")

    def __str__(self):
        return self.name_people
    class Meta:
        verbose_name = 'работкника'
        verbose_name_plural = 'Работкники'

class GroupHome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'Разделы'
    
class NameObject(models.Model):  
    name = models.CharField(max_length=200, verbose_name='Имя объекта')
    group_home = models.ForeignKey(GroupHome, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Раздел')
    info = JSONField(default = default_specific_workouts())

    def __str__(self):
        if self.group_home is None:
            return self.name
        else:
            return f'{self.group_home}: {self.name}'

    class Meta:
        verbose_name = 'имя объекта'
        verbose_name_plural = 'Имена объектов'

