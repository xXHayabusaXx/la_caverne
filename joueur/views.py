from django.shortcuts import render

# Create your views here.

def calcul(request):
    """Display calcul results and save user's personnage information."""

    return render(request, "joueur/perso.html")