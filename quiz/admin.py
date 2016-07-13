from django.contrib import admin

from .models import Quiz
from .models import Question
from .models import Answer
from .models import Result
from .forms import AnswerForm


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('id', 'title', )
    ordering = ('-id', '-created_at', )
    list_filter = ('title', )
    search_fields = ('title', )


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_question_seq', 'created_at',)
    list_display_links = ('id', 'title', )
    ordering = ('-id', '-created_at', )
    list_filter = ('title', )
    search_fields = ('title', )
    form = AnswerForm

    def get_question_seq(self, obj):
        return obj.question.seq



admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result)

