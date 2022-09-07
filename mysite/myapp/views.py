# myapp/views.py
from django.http import HttpResponse


def homepage_view(request):
    return HttpResponse('To have better understanding, try to use /admin url after creating superuser.')