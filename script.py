import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'

django.setup()

from work_searches.models import Vacancy, Company, Specialty

if __name__ == '__main__':
    a = Vacancy(
        title="Разработчик на Python",
        specialty="backend",
        company="3",
        skills="Python, Nginx, Git, Django, Docker, Kubernetes, Высоконагруженные системы",

        salary_min=100000,
        salary_max=150000,
        published_at="2020-03-11"
    )
    print(a)