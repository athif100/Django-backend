from django.shortcuts import render
from django.http import HttpResponse
from.models import Artical
from django.shortcuts import get_object_or_404
from.models import Characters
from.models import Technique
from django.shortcuts import redirect
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
def create_character(request,):
    if request.method =="POST":
        firstname= request.POST.get("firstname")
        print (firstname)
        secondname= request.POST.get("secondname")
        print (secondname)
        discription= request.POST.get("discription")
        print (discription)
        image= request.FILES.get("image")
        print (image)
        newcharacter=Characters(first_name=firstname,second_name=secondname,discription=discription,image=image)
        newcharacter.save()
    return render(request,"Character.html")

def create_techqnique(request,):
    if request.method =="POST":
        red_name= request.POST.get("red_name")
        print (red_name)
        damage_amount= request.POST.get("damage_amount")
        print (damage_amount)
        owner= request.POST.get("owner")
        print (owner)
        owner=Characters.objects.get(pk=int(owner))
        newtechnique=Technique(red_name=red_name,damage_amount=damage_amount,owner=owner)
        newtechnique.save()
    return render (request,"Technique.html")
def show_all_characters(request,):
    #fetch all characters
    all_my_characters= Characters.objects.all() 
    return render (request,"show_allchar.html",{"all_my_characters":all_my_characters})
    
def show_all_techniques(request,):
    #fetch all techniques
    all_my_techniques= Technique.objects.all() 
    return render (request,"show_alltech.html",{"all_my_techniques":all_my_techniques})
def show_1_character(request,id):
    my_character=Characters.objects.get(pk=id) 
    return render (request,"show_1char.html",{"my_character":my_character})

def show_1_technique(request,id):
    my_technique=Technique.objects.get(pk=id) 
    return render (request,"show_1tech.html",{"my_technique":my_technique})
    
def edit_character(request,id):
    my_character=Characters.objects.get(pk=id)
    if request.method =="POST":
        firstname= request.POST.get("firstname")
        print (firstname)
        secondname= request.POST.get("secondname")
        print (secondname)
        discription= request.POST.get("discription")
        print (discription)
        image= request.FILES.get("image")
        print (image)
        my_character.first_name=firstname
        my_character.second_name=secondname
        my_character.discription=discription
        my_character.image=image
        my_character.save()
    return render (request,"edit_char.html",{"my_character":my_character})

def edit_teqnique(request,id):
    my_technique=Technique.objects.get(pk=id)
    if request.method=="POST":
        red_name=request.POST.get("red_name")
        damage_amount=request.POST.get("damage_amount")
        owner=request.POST.get("owner")
        my_technique.red_name=red_name
        my_technique.damage_amount=damage_amount
        #my_technique.owner=owner
        my_technique.save()
    return render (request,"edit_tech.html",{"my_technique":my_technique})
def delete_character(request,id):
    my_character=Characters.objects.get(pk=id)
    my_character.delete()
    return redirect ("homepage")

def delete_technique(request,id):
    my_technique=Technique.objects.get(pk=id)
    my_technique.delete()
    return redirect ("homepage")
