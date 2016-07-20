"""vessel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from quiz import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/$', views.view_quiz, name='quiz'),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/(?P<seq>[0-9]+)/$', views.ask_question, name='question'),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/result$', views.view_result, name='result'),
    url(r'^days/', views.days),
    url(r'^quiz/$', views.quiz),
    url(r'^quiz/all$', views.quiz_all),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
