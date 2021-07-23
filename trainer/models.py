from django.db import models

# Create your models here.
class Trainer(models.Model):
    First_name=models.CharField(max_length=12)
    Last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    Date_Of_Birth=models.DateField()
    Subject=models.CharField(max_length=20)

    
