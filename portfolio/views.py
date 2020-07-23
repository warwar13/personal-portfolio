from django.shortcuts import render
from .models import Project
from blog.models import Blog

# Create your views here.

def home(request):
    projects = Project.objects.all().order_by('-id')
    blogs = Blog.objects.all()
    context = {
        'projects' : projects,
        'blogs' : blogs,
    }

    return render(request,'portfolio/home.html',context)