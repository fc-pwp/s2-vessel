from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

#from quiz.models import Quiz
from .models import Quiz
from .models import Question
from .forms import StartQuizForm


def quiz(request):
    """퀴즈 목록을 보여주는 뷰 함수
    """
    quizzes = Quiz.objects.filter(status='open')
    ctx = {
        'quizzes': quizzes,
    }
    return render(request, 'quiz.html', ctx)


def view_quiz(request, pk):
    """개별 퀴즈를 보여주는 뷰 함수
    """
    q = get_object_or_404(Quiz, id=pk)

    if request.method == 'GET':
        frm = StartQuizForm()
    elif request.method == 'POST':
        frm = StartQuizForm(request.POST)

        if frm.is_valid():
            request.session['userinfo'] = frm.cleaned_data['user']

            return redirect('view_question', quiz_pk=q.pk, question_pk=1)

    ctx = {
        'quiz_view': q,
        'quiz_form': frm,
    }
    return render(request, 'quiz_view.html', ctx)


def view_question(request, quiz_pk, question_pk):
    # question = Question.objects.get(id=question_pk)
    question = get_object_or_404(Question, id=question_pk)
    # 1. Answer.objects.filter(question=question)
    # 2. question.answer_set.all()
    ctx = {
        'question': question,
    }
    return render(request, 'question_view.html', ctx)


