from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import math
import operator

from django.forms import formset_factory
from .models import Question, Quiz, Answer, Result
from .forms import QuizForm, StartQuizForm

import logging

logger = logging.getLogger(__name__)

def days(request):
    questions = Question.objects.all().order_by('seq')
    ctx = { 'questions' : questions }
    return render(request, 'questions.html', ctx)

def quiz_all(request):
    # qz = Quiz.objects.all()
    qz = Quiz.objects.all()
    QuizFormSet = formset_factory(QuizForm)
    formset = QuizFormSet(qz)
    return render(request, 'quiz_all.html', {"formset": formset,})

def quiz(request):
    """퀴즈 목록을 보여주는 뷰 함수
    """
    quizzes = Quiz.objects.filter(status='open')
    ctx = {
        'quizzes': quizzes,
    }
    return render(request, 'quiz.html', ctx)


def view_quiz(request, quiz_pk):
    """개별 퀴즈를 보여주는 뷰 함수
    """
    if request.method == 'GET':
        frm = StartQuizForm()
    else:
        frm = StartQuizForm(request.POST)
        if frm.is_valid():
            logger.error("session init")
            request.session['user'] = frm.cleaned_data['user']
            request.session['quiz'] = {
                'quiz_pk': quiz_pk,
                'question_num': Question.objects.filter(quiz=quiz_pk).count(),
                'answers': {}
            }
            return redirect('question', quiz_pk=quiz_pk, seq=1)

    q = get_object_or_404(Quiz, pk=quiz_pk)
    ctx = {
        'quiz_view': q,
        'quiz_form': frm,
    }
    return render(request, 'quiz_view.html', ctx)

def ask_question(request, quiz_pk, seq):
    # answers = get_object_or_404(Answer, question=question)
    # answers = question.answer_set.all()

    if 'a' in request.GET:
        answer = request.GET['a']
        get_object_or_404(Result, quiz__id=quiz_pk, value=answer)
        
        request.session.modified = True
        request.session['quiz']['answers'][request.GET['q']] = answer
        if int(seq) > request.session['quiz']['question_num']:
            return redirect('result', quiz_pk)

    question = get_object_or_404(Question,
                                quiz__id=quiz_pk,
                                quiz__status='open',
                                seq=seq)

    ctx = {
        'question': question,
    }
    return render(request, 'question_view.html', ctx)

def view_result(request, quiz_pk):
    answer_values = request.session['quiz']['answers'].values()
    count_by_answer = {}
    for v in answer_values:
        count_by_answer[v] = count_by_answer.get(v,0) + 1
    sorted_answers = sorted(count_by_answer.items(), key=operator.itemgetter(1), reverse=True)
    result = get_object_or_404(Result, quiz__id=quiz_pk, value=sorted_answers[0][0])
    ctx = {
        # 'content': rs.content,
        'content': result.content
    }
    return render(request, 'result.html', ctx)

def create_quiz(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuizForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/quiz/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuizForm()

    return render(request, 'quiz.html', {'form': form})
