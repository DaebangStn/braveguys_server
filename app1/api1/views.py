from django.http.response import Http404
from django.http import HttpResponse

from .models import State


def open(request):
    state = State()
    state.motor = True
    state.save()
    return HttpResponse("submitted")


def close(request):
    state = State()
    state.motor = False
    state.save()
    return HttpResponse("submitted")


def state(request):
    try:
        state_recent = State.objects.last()
    except:
        raise Http404("no item")

    print(state_recent)
    return HttpResponse("hi")

