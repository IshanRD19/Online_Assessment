from django.db import models
from Student.models import *
# Create your models here.

class Questions(models.Model):
    questionID = models.CharField(primary_key=True, max_length=10)
    statement = models.TextField(max_length=200)
    optionA = models.CharField(max_length=50)
    optionB = models.CharField(max_length=50)
    optionC = models.CharField(max_length=50)
    optionD = models.CharField(max_length=50)
    correctOption = models.CharField(max_length=1)
    image1 = models.ImageField(upload_to = 'pic_folder/', default = None)
    image2 = models.ImageField(upload_to = 'pic_folder/', default = None)
    maxMarks = models.DecimalField(max_digits=6, decimal_places=3)
    subject = models.CharField(max_length=20, default='NA')
    subCategory = models.CharField(max_length=20, )
    difficultyLevel = models.IntegerField(default=2)        # 1 to 5 for increasing toughness
    timeLimit = models.DecimalField(max_digits=8, decimal_places=3)

class Question_Papers(models.Model):
    qpID = models.CharField(primary_key=True, max_length=20)
    qpName = models.CharField(max_length=30)
    timeDuration = models.DecimalField(max_digits=8, decimal_places=3)
    createdOn = models.DateField(auto_now=True)
    activeFlag = models.BooleanField(default=False)

class Records(models.Model):
    recordID = models.CharField(primary_key=True, max_length=10)
    fromTime = models.TimeField(auto_now=True)
    tillTime = models.TimeField(auto_now=True)
    studentID = models.ForeignKey(Students)
    questionID = models.ForeignKey(Questions)
    response = models.CharField(max_length=2)

