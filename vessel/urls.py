from django.conf.urls import url
from django.contrib import admin

#from quiz.views import quiz
from quiz import views as quiz_views


urlpatterns = [
    url(r'^$', quiz_views.quiz),
    url(r'^quiz/([0-9]+)/$', quiz_views.view_quiz),
    url(r'^admin/', admin.site.urls),
]
