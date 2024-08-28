from django.shortcuts import render
from .models import Settings, Services

# Create your views here.
def home(request):
    settings = Settings.objects.all().first()
    services = Services.objects.all()
    return render(request, 'portfolio/index.html', {'settings': settings, 'services': services})