from django.shortcuts import render
from .models import *
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
    card = Card.objects.get(id=id) # 1 tane ürün getir
    
    context = {
        "card":card,
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
