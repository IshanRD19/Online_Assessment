from django.shortcuts import render, redirect
from Question_Bank.models import *
import pandas as pd
from django.http import HttpResponse
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


def createquestionpaper(request):
    questions = Questions.objects.all()
    return render(request, 'createquestionpaper.html', {'context': questions})


def submitquestionpaper(request):
    if request.method == 'POST':
        question_paper = Question_Papers()
        question_paper.qpName = request.POST['qname']
        all_questions = Questions.objects.all()
        # s = []
        question_paper.save()
        for i in all_questions:
            try:
                if request.POST[str(i.id)]:
                # s.append(i.statement)
                    question_paper.questions.add(i)
            except:
                pass
        question_paper.save()
        return HttpResponse('<h1>Created Successfully</h1><br><a href="/">GO BACK</a>')
    return redirect('/')

