from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#from quiz.views import quiz
from quiz import views as quiz_views


urlpatterns = [
    url(r'^$', quiz_views.quiz, name='list_quiz'),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/question/(?P<seq>[0-9]+)/$',
        quiz_views.view_question,
        name='view_question'),
    url(r'^quiz/(?P<pk>[0-9]+)/$', quiz_views.view_quiz, name='view_quiz'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

