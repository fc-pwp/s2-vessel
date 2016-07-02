from django.db import models


class Quiz(models.Model):
    _choices = [
        ('open', '열림'),
        ('close', '종료'),
        ('draft', '작성 중'),
    ]
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=5, choices=_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    seq = models.SmallIntegerField()
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='%Y/%m/%d/')
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

