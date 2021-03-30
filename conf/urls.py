"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from work_searches import views

handler404 = views.custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('vacancies/', views.vacancies_view, name='vac'),
    path('vacancies/cat/<str:code>', views.spec_vacancies_view),
    path('vacancies/<int:pk>/', views.vacancy_view),
    path('companies/<int:pk>/', views.companies_view),

]
