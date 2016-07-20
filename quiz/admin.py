from django.contrib import admin

from .models import Quiz, Question, Answer, Result

# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('title',)
    ordering = ('id', )
    search_fields = ('title', 'content', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('seq', 'title', 'created_at')
    list_display_links = ('title',)
    ordering = ('id', 'created_at')
    search_fields = ('title', 'content', )
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'number', 'content')
    list_display_links = ('number','content',)
    ordering = ('number',)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('value', 'min_value', 'max_value', 'content')
    list_display_links = ('value','content')
    ordering = ('value',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
