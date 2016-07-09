from django.db import models


class Quiz(models.Model):
    _choices = [
        ('open', '열림'),
        ('close', '종료'),
        ('draft', '작성 중'),
    ]
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=5, choices=_choices)
    result = models.ManyToManyField('Result')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    seq = models.SmallIntegerField()
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='questions/%Y/%m/%d/')
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=250)
    number = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='answers/%Y/%m/%d/',
                              null=True,
                              blank=True)
    value = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('question', 'number', ),
            ('question', 'value', ),
        )


class Result(models.Model):
    value = models.CharField(max_length=1)
    min_value = models.SmallIntegerField()
    max_value = models.SmallIntegerField()
    image = models.ImageField(upload_to='results/%Y/%m/%d/')
    content = models.TextField(null=False)
    is_excepted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

