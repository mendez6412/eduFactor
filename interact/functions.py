from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
import random


def get_ten_random_questions(model, flavor):
    questions = model.objects.filter(flavor=flavor)
    questions = list(questions)
    random.seed(42)
    random.shuffle(questions)
    questions = questions[:10]
    return questions


def page_handler(questions, request):
    paginator = Paginator(questions, 1)
    page = request.GET.get('page')
    context = {}
    try:
        pager = paginator.page(page)
        question = pager[0]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pager = paginator.page(1)
        question = pager[0]
    context['pager'] = pager
    context['question'] = question
    return pager, question, context
