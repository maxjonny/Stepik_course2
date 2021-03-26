from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'hello')


def vacancies_view(request):
    return render(request, 'hello')


def companies_view(request, pk):
    return render(request, 'hello')

