from django.db import models

# Create your models here.

class Students(models.Models):
    studentID = models.CharField(primary_key=True, max_length=10)