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


def editquestions(request):
    all_questions = Questions.objects.all()
    return render(request, 'allquestionsforedit.html', {'context': all_questions})


def editquestionid(request, question_id):
    question = Questions.objects.get(id=question_id)
    return render(request, 'editquestion.html', {'context': question})


def questionedit(request, question_id):
    if request.method == 'POST':
        question = Questions.objects.get(id=question_id)
        question.statement = str(request.POST['statement'])
        question.correctOption = str(request.POST['correct'])
        question.incorrectOption1 = str(request.POST['incorrect1'])
        question.incorrectOption2 = str(request.POST['incorrect2'])
        question.incorrectOption3 = str(request.POST['incorrect3'])
        question.maxMarks = str(request.POST['marks'])
        question.subject = str(request.POST['subject'])
        question.subCategory = str(request.POST['subcategory'])
        question.difficultyLevel = str(request.POST['difficulty'])
        question.timeLimit = str(request.POST['time'])
        question.save()
        return HttpResponse('<h1>Altered Successfully</h1><br><a href="/">GO BACK</a>')

    return redirect('/')


def editquestionpaper(request):
    all_question_papers = Question_Papers.objects.all()
    return render(request, 'questionpapersforedit.html', {'context': all_question_papers})


def questionpaperid(request, questionpaper_id):
    question_paper = Question_Papers.objects.get(id=questionpaper_id)
    all_questions = Questions.objects.all()
    return render(request, 'editquestionpaper.html', {'question_paper': question_paper, 'questions': all_questions})


def questionpaperedit(request, questionpaper_id):
    if request.method == 'POST':
        question_paper = Question_Papers.objects.get(id=questionpaper_id)
        question_paper.qpName = request.POST['qpname']
        all_questions = Questions.objects.all()
        if request.POST['active']:
            question_paper.activeFlag = True
        else:
            question_paper.activeFlag = False
        # s = []
        question_paper.save()
        for i in all_questions:
            try:
                if request.POST[str(i.id)]:
                # s.append(i.statement)
                    question_paper.questions.add(i)
                else:
                    question_paper.question.exclude(i)
            except:
                pass
        question_paper.save()
        return HttpResponse('<h1>Created Successfully</h1><br><a href="/">GO BACK</a>')
    return redirect('/')

