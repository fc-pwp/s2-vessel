from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

#from quiz.models import Quiz
from .models import Quiz
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
    if request.method == 'GET':
        frm = StartQuizForm()
    elif request.method == 'POST':
        frm = StartQuizForm(request.POST)

        if frm.is_valid():
            return HttpResponse('유효하지만, 구현은 다음 수업에서...')

    q = get_object_or_404(Quiz, id=pk)
    ctx = {
        'quiz_view': q,
        'quiz_form': frm,
    }
    return render(request, 'quiz_view.html', ctx)

