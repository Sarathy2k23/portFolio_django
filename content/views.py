from django.shortcuts import render
from .models import content

def about_view(request):
    about = content.objects.first()
    return render(request, 'content/content.html', {'content': about})

