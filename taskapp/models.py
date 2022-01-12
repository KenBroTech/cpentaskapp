from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    

    def __str__(self):
        return self.task
