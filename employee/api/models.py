from django.db import models
from django.forms.models import model_to_dict
from employee.settings import PUBLISH_CHANNEL

from .pub import publish_data_on_redis


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    department = models.ForeignKey(to='Department', on_delete=models.CASCADE)
    manager = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    title = models.CharField(max_length=255)

    parent_department = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class PositionId(models.Model):
    position_id = models.IntegerField()
    employee_id = models.ForeignKey(to='Employee', on_delete=models.CASCADE, related_name='positions')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        message = model_to_dict(self)
        publish_data_on_redis(PUBLISH_CHANNEL, message)
        print(message)
