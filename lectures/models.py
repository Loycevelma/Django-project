from django.db import models

# Create your models here.
class Lectures(models.Model):
    Course_Name=models.CharField(max_length=20)
    Course_Trainer=models.CharField(max_length=12)
    Course_Description=models.CharField(max_length=35)
    Course_Duration=models.IntegerField()
    
