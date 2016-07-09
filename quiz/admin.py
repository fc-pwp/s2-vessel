from django.contrib import admin

from .models import Quiz
from .models import Question
from .models import Answer
from .models import Result


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('id', 'title', )
    ordering = ('-id', '-created_at', )
    list_filter = ('title', )
    search_fields = ('title', )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)

