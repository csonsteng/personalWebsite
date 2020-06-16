from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def projects(request):
    return render(request, 'home/projects.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-date','-id')
    context = {
        'blogs': blogs,
        }
    return render(request, 'home/blog.html', context)

def regionMap(request):
    return render(request, 'home/map.html')
