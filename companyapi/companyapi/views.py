from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from .forms import PostForm
def home(request):
    friends=["nischal","suraj","bishal"]
    #return HttpResponse("this is home page")
    return JsonResponse(friends,safe=False)