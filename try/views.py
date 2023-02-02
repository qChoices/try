from django.http import HttpResponse


def a(request):
    return HttpResponse('<h1>Hello</h1>')