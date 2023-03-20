
from django.shortcuts import get_object_or_404, redirect, render

from order.models import Commande
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from product.models import Product
from .models import  Commande

# Create your views here.
def order(request):
    orders = Commande.objects.all()
    return render(request, 'order/commande.html', {'orders': orders})



@login_required
def produit_detail(request, produit_id):
    product = get_object_or_404(Product, id=produit_id)

    if request.method == 'POST':
        address = request.POST['address'] 
        ville = request.POST['ville'] 
        pays = request.POST['pays'] 
        zipcode = request.POST['zipcode'] 
        commande = Commande(users=request.user , product=product ,address=address, ville=ville, pays=pays, zipcode=zipcode)
        commande.save()
        return redirect('confirmation')
    else: 
        return render(request, 'order/checkout.html')

def confirmation(request):

    nom_utilisateur = request.user.username
    context = {'nom_utilisateur': nom_utilisateur}

    return render(request, 'order/comfirmation.html', context)

