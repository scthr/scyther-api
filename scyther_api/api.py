import json
import logging

from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django_eventstream import send_event

from scyther_api.utils import restrict_methods


@restrict_methods("GET")
def healthcheck(request):
    return HttpResponse("Alles in Ordnung.")


@csrf_exempt
@restrict_methods("POST")
def move(request):
    body_parsed = json.loads(request.body)
    logging.info(body_parsed)
    send_event("broadcast", "message", f"Making move {body_parsed}!")
    return HttpResponse(200)


urlpatterns = [
    path("health/", healthcheck),
    path("move/", move),
]
