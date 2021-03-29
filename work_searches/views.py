from django.shortcuts import render
from work_searches.models import Vacancy, Company
# Create your views here.
all_vacancies = Vacancy.objects.all()
print(all_vacancies)


def index_view(request):
    return render(request, 'hh/index.html')


def spec_vacancies_view(request, code):
    context = '(вакансии по специализации)'
    return render(request, 'hh/vacancies.html', context={
        'context': context
    })


def vacancies_view(request):
    return render(request, 'hh/vacancies.html', context={
        'vacancies_count': all_vacancies.count(),
        'all_vacancies': all_vacancies
        })



def vacancy_view(request, pk):
        vacancy_pk = all_vacancies.get(id=pk)
        return render(request, 'hh/vacancy.html', context={'vacancy': vacancy_pk})


def companies_view(request, pk):
    return render(request, 'hh/company.html', context={
        'company': Company.objects.get(id=pk),
    })




