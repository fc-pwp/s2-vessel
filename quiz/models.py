from django.db import models

# Create your models here.

class Quiz(models.Model):
    _choices = [
        ('open', '열림'),
        ('close', '종료'),
        ('draft', '작성중'),
    ]
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=5, choices=_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} - {}'.format(self.title, self.status)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    seq = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='question/%Y/%m/%d', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.seq, self.title)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    number = models.PositiveSmallIntegerField()
    content = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=1)
    image = models.ImageField(upload_to="answers/%Y/%m/%d", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        unique_together = (
            ('question', 'number', ),
            ('question', 'value', ),
        )

class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    value = models.CharField(max_length=1)
    min_value = models.SmallIntegerField()
    max_value = models.SmallIntegerField()
    content = models.TextField(null=False)
    is_excepted = models.BooleanField()
    image = models.ImageField(upload_to="answers/%Y/%m/%d", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
