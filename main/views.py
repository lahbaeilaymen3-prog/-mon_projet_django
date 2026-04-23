from django.shortcuts import render, get_object_or_404
from .models import Livraison

def index(request):
    livraisons = Livraison.objects.all()
    return render(request, 'main/index.html', {'livraisons': livraisons})

def detail_livraison(request, id):
    livraison = get_object_or_404(Livraison, id=id)
    return render(request, 'main/detail.html', {'livraison': livraison})
    