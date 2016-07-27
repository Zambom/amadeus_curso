from django.shortcuts import render

def index(request):
	return render(request, "app/index.html")

def test(request):
	return render(request, "admin_index.html")

def modulos_curso(request):
	return render(request, "admin_modulos_curso.html")

def participantes_curso(request):
	return render(request, "admin_participantes_curso.html")

def avaliacao_curso(request):
	return render(request, "admin_avaliacao_curso.html")

def email(request):
	return render(request, "admin_send_email.html")

def profile(request):
	return render(request, "admin_profile.html")

def edit_profile(request):
	return render(request, "admin_editar_perfil.html")

def reset_pass(request):
	return render(request, "admin_reset_pass.html")

def colegas(request):
	return render(request, "admin_colegas_curso.html")

def configuracoes(request):
	return render(request, "admin_config.html")

def mobile(request):
	return render(request, "mobile.html")

def tarefas(request):
	return render(request, "admin_tarefas.html")

def users_online(request):
	return render(request, "admin_online.html")

def search(request):
	return render(request, "admin_search.html")