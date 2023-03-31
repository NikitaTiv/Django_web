from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse('<h1>Website about Cats</h1>')


def index_num(request, catid):
    if catid > 10:
        return redirect('home')
    return HttpResponse(f'<h1>Website about Cats</h1><p>{catid}</p>')
