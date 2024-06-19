from django.shortcuts import render
from .models import projects

# Create your views here.


def project_list_view(request):
    projects = projects.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

