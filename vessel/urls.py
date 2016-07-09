from django.conf.urls import url
from django.contrib import admin

#from quiz.views import quiz
from quiz import views as quiz_views


urlpatterns = [
    url(r'^$', quiz_views.quiz),
    url(r'^admin/', admin.site.urls),
]
