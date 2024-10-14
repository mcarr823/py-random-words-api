from django.http import HttpResponse, JsonResponse
from random import choice
from .models import Word


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def random(request):
    # Grab a list of primary keys, instead of querying the objects,
    # for efficiency reasons
    pks = Word.objects.values_list('pk', flat=True)

    # Pick a random primary key
    random_pk = choice(pks)

    # Grab the object which corresponds to this primary key
    word = Word.objects.get(pk=random_pk)

    # And return it
    return JsonResponse([word.text], safe=False)

def randomLength(request, length):
    pks = Word.objects.filter(length=length).values_list('pk', flat=True)
    random_pk = choice(pks)
    word = Word.objects.get(pk=random_pk)
    return JsonResponse([word.text], safe=False)

def all(request):
    words = Word.objects.values_list('text', flat=True)
    words = list(words)
    return JsonResponse(words, safe=False)

def allLength(request, length):
    words = Word.objects.filter(length=length).values_list('text', flat=True)
    words = list(words)
    return JsonResponse(words, safe=False)
