from django.shortcuts import render, redirect, HttpResponse # sayfaya yönlendirir
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
# Create your views here.


def index(request):
    cards = Card.objects.all().order_by("?")[0:3]
    try:
        category = Category.objects.get(id=1)
        cardsg = Card.objects.get( brand = category ) # 1 ürün getir
    except:
        cardsg = Card.objects.filter(brand=category)[0]
    cardsf = Card.objects.filter(brand = category) # ürünleri filtrele
    
    context={
        "cards": cards,
        "cardsg": cardsg,
        "cardsf": cardsf,
    }
    
    return render(request, 'index.html', context)

def Detail(request,id):

    print(request.path)
    
    card = Card.objects.get(id=id) # 1 tane ürün getir
    comments = Comment.objects.filter(card=card)
    
    
    if request.method == "POST":
        name2 = request.POST["name"]
        title2 = request.POST["title"]
        text2 = request.POST["text"]
        
        comment = Comment(name=name2,title=title2, text=text2, card=card)
        comment.save()
        return redirect("/detay/" + id + "/")

    context = {
        "card":card,
        "comments":comments,
    }
    
    return render(request,'detail.html',context)

def allProduct(request, brandurl="All"):
    
    if brandurl != "All" :
        category = Category.objects.get(title__icontains = brandurl)
        cards = Card.objects.filter(brand=category)
    else:
        cards = Card.objects.all()
    
    context = {
        "cards": cards
    }
    return render(request,'allproduct.html',context)


# USER
def loginUser(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password) # kullanıcının olup olmadığını kontrol eder, eğer yoksa değeri None'dır
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            context.update({"hata":"Kullanıcı adı veya şifre yanlış!"})
        
    return render(request,"users/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def registerUser(request):
    context={}
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name, last_name=surname)
                user.save()
                return redirect('loginUser')
            else:
                context.update({"hata": "Kullanıcı adı daha önceden alınmış!"})
            
    return render(request,'users/register.html',context)
