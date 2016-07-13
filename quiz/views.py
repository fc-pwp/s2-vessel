from django.shortcuts import render

#from quiz.models import Quiz
from .models import Quiz


def quiz(request):
    """퀴즈 목록을 보여주는 뷰 함수
    """
    quizzes = Quiz.objects \
            .filter(status='open')
    ctx = {
        'quizzes': quizzes,
    }
    return render(request, 'quiz.html', ctx)


def view_quiz(request, pk):
    """개별 퀴즈를 보여주는 뷰 함수
    """
    ctx = {}
    return render(request, 'quiz_view.html', ctx)
