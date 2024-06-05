import socket
import time
from http import HTTPStatus

from django.conf import settings
from django.http import JsonResponse


def health_check(request):
    uptime = time.time() - settings.APP_START_TIME
    return JsonResponse({
        "status": "ok",
        "uptime": uptime,
        "hostname": socket.gethostname(),
        "ip_address": request.META.get('REMOTE_ADDR')
    }, status=HTTPStatus.OK)