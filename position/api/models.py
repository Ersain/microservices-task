from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class EmployeeIds(models.Model):
    employee_id = models.IntegerField()
    position_id = models.ForeignKey(to='Position', on_delete=models.CASCADE)
