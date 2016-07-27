from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "index.html")

def nova_conta(request):
	return render(request, "nova_conta.html")

def lembrar_senha(request):
	return render(request, "lembrar_senha.html")