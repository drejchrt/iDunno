from django.db import models
from django import forms
import random

COLORS = [
        ('B', 'Blue'),
        ('G', 'Green'),
        ('R', 'Red'),
        ('Y', 'Yellow')
    ]

class Question(models.Model):
    COLORS = {
        'B':'#009ce5',
        'G':'#33ac2d',
        'R':'#e50c07',
        'Y':'#fdc500',
    }

    question = models.TextField()
    hint3 = models.TextField()
    hint2 = models.TextField()
    hint1 = models.TextField()
    answer = models.TextField()
    color = models.CharField(
        max_length=10,
        choices=[
            ('B', 'Blue'),
            ('G', 'Green'),
            ('R', 'Red'),
            ('Y', 'Yellow')
        ]
    )
    @staticmethod
    def get_random_question(color=None):
        if color is None:
            color = COLORS[random.randint(0,3)][0]
        qs = Question.objects.all().filter(color=color)
        return qs[random.randint(0,len(qs)-1)]


