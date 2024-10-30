from django.shortcuts import render
from .models import Skill


# def index(request):
#     skills = Skill.objects.all()
#     return render(request, 'skills/skills_page.html', {'skills': skills})


def skills_page(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skills_page.html', {'skills': skills})
