from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'hh/index.html')


def spec_vacancies_view(request):
    context = '(вакансии по специализации)'
    return render(request, 'hh/vacancies.html', context={
        'context': context
    })


def vacancies_view(request):
        context = '(Здесь будут все вакансии)'
        return render(request, 'hh/vacancies.html', context={
            'context': context
        })


def vacancy_view(request, pk):
        return render(request, 'hh/vacancy.html')


def companies_view(request, pk):
    return render(request, 'hh/company.html')

