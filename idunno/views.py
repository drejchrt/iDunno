from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

from idunno.models import Question
from idunno.forms import NewQuestionForm

import json


def index(request):
    question = Question.get_random_question()

    context = {
        'index': True,
        'id': question.pk,
        'question': question.question,
        'hint3': question.hint3,
        'hint2': question.hint2,
        'hint1': question.hint1,
        'answer': question.answer,
        'color': Question.COLORS[question.color]
    }
    return render(request, 'idunno/index.html', context)


def add_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=True)
            new_question.save()
            return redirect('index')

    else:
        form = NewQuestionForm()
    return render(request, 'idunno/newQuestion.html', {'form': form})


def list(request, sort_attr='id'):
    questions = Question.objects.all().order_by(sort_attr)
    context = {'questions': questions}
    return render(request, "idunno/list.html", context)


def edit_question(request, question_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = Question.objects.get(pk=question_id)
            question.color = data['color']
            question.question = data['question']
            question.hint3 = data['hint3']
            question.hint2 = data['hint2']
            question.hint1 = data['hint1']
            question.answer = data['answer']
            print(question)
            question.save()
        except Exception:
            return HttpResponse(json.dumps({'succes': False}))

        return HttpResponse(json.dumps({'success': True}))
    else:
        question = Question.objects.get(pk=question_id)
        context = {
            'id': question.pk,
            'question': question.question,
            'hint3': question.hint3,
            'hint2': question.hint2,
            'hint1': question.hint1,
            'answer': question.answer,
            'color': Question.COLORS[question.color]
        }
        return render(request, 'idunno/question_edit.html', context)


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'id': question.pk,
        'question': question.question,
        'hint3': question.hint3,
        'hint2': question.hint2,
        'hint1': question.hint1,
        'answer': question.answer,
        'color': Question.COLORS[question.color]
    }
    return render(request, 'idunno/question.html', context)


def game(request, query):
    try:
        query = int(query)
        question = Question.objects.get(pk=query)
    except ValueError:
        color = None if query == '?' else query
        question = Question.get_random_question(color)

    context = {
        'index': True,
        'id': question.pk,
        'question': question.question,
        'hint3': question.hint3,
        'hint2': question.hint2,
        'hint1': question.hint1,
        'answer': question.answer,
        'color': Question.COLORS[question.color]
    }
    return render(request, 'idunno/game.html', context)


def search(request, query):
    context = {}
    questions = Question.objects.filter(
        Q(question__icontains=query) |
        Q(hint3__icontains=query) |
        Q(hint2__icontains=query) |
        Q(hint1__icontains=query) |
        Q(answer__icontains=query)
    )
    context["query"] = query
    context["questions"] = questions
    # print(questions)
    return render(request, "idunno/list.html", context=context)
