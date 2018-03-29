from django.db import models
#from Question_Bank.models import *
# Create your models here.

class Students(models.Model):
    studentID = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, default='NA')
    password = models.CharField(max_length=15, default='123456')

class Student_Response(models.Model):
    studentID = models.ForeignKey(Students)             # index will be primary key by default
    qpID = models.ForeignKey('Question_Bank.Question_Papers')
    questionID = models.ForeignKey('Question_Bank.Questions')
    response = models.CharField(max_length=2)
    correctOption = models.CharField(max_length=2)
    marks = models.DecimalField(max_digits=6, decimal_places=3)

class Student_Summary(models.Model):
    studentID = models.ForeignKey(Students)
    score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel1Score = models.DecimalField(max_digits=8, decimal_places=3)     # easiest
    difficultyLevel2Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel3Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel4Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel5Score = models.DecimalField(max_digits=8, decimal_places=3)     # toughest

class Student_Attempt_Result_Summary(models.Model):
    qpID = models.ForeignKey('Question_Bank.Question_Papers')
    studentID = models.ForeignKey(Students)
    attemptedFlag = models.BooleanField(default=False)
    startTime = models.TimeField(auto_now=True)
    endTime = models.TimeField(auto_now=False)
    difficultyLevel1Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel2Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel3Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel4Score = models.DecimalField(max_digits=8, decimal_places=3)
    difficultyLevel5Score = models.DecimalField(max_digits=8, decimal_places=3)


