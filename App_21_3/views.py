# views.py
from django.shortcuts import render
from .models import Profile, Project

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, 'home.html', {'profile': profile, 'projects': projects})
