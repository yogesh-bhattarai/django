from django.shortcuts import render, HttpResponse
#from .forms import PostForm 
def new(request):
    return render(request,"blog/about.html")
def order(request):
    return render(request,"blog/order.html")
