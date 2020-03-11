from django.shortcuts import render
from .models import BlogArticle

# Create your views here.
def title(request):
    blogs = BlogArticle.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})
