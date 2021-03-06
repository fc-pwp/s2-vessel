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

    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    seq = models.SmallIntegerField()
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='questions/%Y/%m/%d/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.seq, self.title)

    def has_next_question(self):
        return Question.objects \
            .filter(quiz__pk=self.quiz.pk, seq=self.seq+1).exists()


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

    def __str__(self):
        return self.title


class Result(models.Model):
    value = models.CharField(max_length=1)
    min_value = models.SmallIntegerField()
    max_value = models.SmallIntegerField()
    image = models.ImageField(upload_to='results/%Y/%m/%d/')
    content = models.TextField(null=False)
    is_excepted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

