from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    cards = Card.objects.all()
    
    context={
        "cards": cards,
    }
    
    return render(request, 'index.html', context)

def Detail(request,id):
    card = Card.objects.get(id=id) 
    
    context = {
        "card":card,
    }
    
    return render(request,'detail.html',context)
