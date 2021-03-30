from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseNotFound

from work_searches.models import Vacancy, Company, Specialty

# Create your views here.


def index_view(request):
    return render(request, 'hh/index.html', context={
        'specs': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })


def spec_vacancies_view(request, code):
    context = get_object_or_404(Specialty, code=code)
    return render(request, 'hh/spec_vacancies.html', context={
        'context': context,
        'specs': Specialty.objects.all(),
    })


def vacancies_view(request):
    all_vacancies = Vacancy.objects.all()
    return render(request, 'hh/vacancies.html', context={
        'all_vacancies': all_vacancies,
        })


def vacancy_view(request, pk):
    vacancy_pk = get_object_or_404(Vacancy, id=pk)
    return render(request, 'hh/vacancy.html', context={'vacancy': vacancy_pk})


def companies_view(request, pk):
    company = get_object_or_404(Company, id=pk)
    return render(request, 'hh/company.html', context={
        'company': company,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Error404<br>Ой, что то сломалось... <br> Это не ваша вина (но это не точно)')
