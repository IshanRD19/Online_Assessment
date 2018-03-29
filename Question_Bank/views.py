from django.shortcuts import render, redirect
from Question_Bank.models import *
import pandas as pd
# Create your views here.


def index(request):
    return render(request, 'home.html')


def createtest(request):
    return render(request, 'createtest.html')


def uploadquestions(request):
    return render(request, 'uploadquestions.html')


def submitquestions(request):
    if request.method == 'POST':
        csv_file = request.FILES['ques']
        dataFrame = pd.read_csv(csv_file)
        for i in range(dataFrame.shape[0]):
            question = Questions()
            question.subject = dataFrame[dataFrame.columns[0]][i]
            question.subCategory = dataFrame[dataFrame.columns[1]][i]
            question.timeLimit = dataFrame[dataFrame.columns[2]][i]
            question.maxMarks = dataFrame[dataFrame.columns[3]][i]
            question.statement = dataFrame[dataFrame.columns[4]][i]
            question.correctOption = dataFrame[dataFrame.columns[5]][i]
            question.incorrectOption1 = dataFrame[dataFrame.columns[6]][i]
            question.incorrectOption2 = dataFrame[dataFrame.columns[7]][i]
            question.incorrectOption3 = dataFrame[dataFrame.columns[8]][i]
            question.save()
        return redirect('/')