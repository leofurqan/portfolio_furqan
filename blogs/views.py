from django.shortcuts import render
from .models import Blogs

# Create your views here.
def blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs': blogs})
