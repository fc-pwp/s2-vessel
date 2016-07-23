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

            return redirect('view_question', quiz_pk=q.pk, seq=1)

    ctx = {
        'quiz_view': q,
        'quiz_form': frm,
    }
    return render(request, 'quiz_view.html', ctx)


def view_question(request, quiz_pk, seq):
    answer_pk = request.GET.get('answer')
    seq = int(seq)
    # question = Question.objects.get(id=question_pk)
    question = get_object_or_404(Question,
            quiz__id=quiz_pk,
            quiz__status='open',
            seq=seq)
    # 1. Answer.objects.filter(question=question)
    # 2. question.answer_set.all()

    if answer_pk and seq > 1:
        prev_question = get_object_or_404(Question,
                quiz__id=quiz_pk,
                quiz__status='open',
                seq=question.seq-1)

        if not prev_question.answer_set.filter(id=answer_pk).exists():
            raise Exception('이상한 없는 답 고르지 마')

        question_and_answer = {
            'question_pk': prev_question.pk,
            'answer_pk': answer_pk,
        }

        #if not isinstance(request.session.get('answers']), dict):
        #    request.session['answers'] = {}
        if 'answers' in request.session:
            if not isinstance(request.session['answers'], dict):
                request.session['answers'] = {}
        else:
            request.session['answers'] = {}

        if not isinstance(request.session['answers'].get(quiz_pk), list):
            request.session['answers'][quiz_pk] = []

        for i, item in enumerate(request.session['answers'][quiz_pk]):
            if item['question_pk'] == question_and_answer['question_pk']:
                request.session['answers'][quiz_pk][i]['answer_pk'] = \
                question_and_answer['answer_pk']
                break
        else:
            request.session['answers'][quiz_pk].append(question_and_answer)

    ctx = {
        'question': question,
    }
    return render(request, 'question_view.html', ctx)


