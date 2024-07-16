from django.shortcuts import render
from .models import Skills, Project
# Create your views here.
def home(request):
    all_skills = Skills.objects.all()[:] # get all instances of skills
    all_projects = Project.objects.all()[:]
    context = {"skills": all_skills, "projects":all_projects}
    return render(request,"myportfolio/home.html", context)