from django.shortcuts import render
from django.http import HttpResponse
from.models import Artical
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage (request):
    return HttpResponse("hello from python") 
def about(request):
    return HttpResponse("hello from homepage") 
def prizing (request): 
    return HttpResponse("your tatal is 300 shillings")
def contact (request): 
    return HttpResponse("your email is athif.gmail")
def profile (request): 
    return HttpResponse("<h1>your profile will look like this</h1><button> click here </button>")
def fav_anime (request): 
    return render(request, "contact.html")
def disliked_anime (request): 
    return render(request, "dislikes.html")
def read_Artical(request,number):
    requested_artical= get_object_or_404(Artical,pk=number)
    #requested_artical=Artical.objects.get(pk=number)
    return render(request, "read.html",{"requested_artical":requested_artical})
def create_artical(request,):
    if request.method =="POST":
        print(request.POST)
        title=request.POST.get("title")
        content=request.POST.get("content")
        print(title)
        print(content)
        new_Artical=Artical(name=title,content=content)
        new_Artical.save()
    return render(request,"create_artical.html")