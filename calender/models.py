from django.db import models

# Create your models here.
class Calender(models.Model):
    Year=models.IntegerField()
    Months=models.IntegerField()
    Days=models.IntegerField()
    Date=models.DateTimeField()
    Course_Duration=models.IntegerField()
    

