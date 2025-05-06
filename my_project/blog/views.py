from django.shortcuts import render
#from .forms import PostForm 
def new(request):
    return render(request,"blog/about.html")
