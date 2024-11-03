from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    isdone= models.BooleanField(default=False)
    untildate = models.DateField()
