from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
	return render(request,"blog/home.html")

def sobre(request):
	return render(request,"blog/sobre.html")

def contato(request):
	return render(request,"blog/contato.html")

def games(request):
	return render(request,"blog/games.html")