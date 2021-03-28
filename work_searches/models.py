from django.db import models

# Create your models here.


class Vacancy(models.Model):
    title = models.CharField(max_length=50),
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name="vacancies"),
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="vacancies"),
    skills = models.CharField(max_length=100),
    description = models.TextField,
    salary_min = models.IntegerField,
    salary_max = models.PositiveIntegerField,
    published_at = models.DateField,


class Company(models.Model):
    name = models.CharField(max_length=50),
    location = models.CharField(max_length=20),
    logo = models.URLField(default='https://place-hold.it/100x60'),
    description = models.CharField(max_length=500),
    employee_count = models.PositiveSmallIntegerField,


class Specialty(models.Model):
    code = models.CharField(max_length=15),
    title = models.CharField(max_length=15),
    picture = models.URLField(default='https://place-hold.it/100x60')


