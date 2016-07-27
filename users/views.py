from django.shortcuts import render

def index(request):
	return render(request, "users/index.html")

def create(request):
	return render(request, "users/create.html")

def update(request):
	return render(request, "users/update.html")

def view(request):
	return render(request, "users/view.html")