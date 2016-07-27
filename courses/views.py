from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from slugify import slugify
from .forms import CourseForm, CategoryForm, ModuleForm

from .models import Course, Module, Category

def index(request):
	context = {
		'courses': Course.objects.all(),
		'categories': Category.objects.all()
	}

	return render(request, "course/index.html", context)

def create(request):
	context = {}

	form = CourseForm(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		course = form.save(commit = False)
		course.slug = slugify(course.name)

		course.save()

		messages.success(request, 'Curso criado com sucesso!')

		return redirect('app:course:manage')
	
	context['form'] = form

	return render(request, "course/create.html", context)

def update(request, slug):
	context = {}
	
	course = get_object_or_404(Course, slug = slug)

	if request.method == 'POST':
		form = CourseForm(request.POST, request.FILES, instance = course)
	
		if form.is_valid():
			course = form.save(commit = False)
			course.slug = slugify(course.name)

			course.save()

			form = CourseForm()

			messages.success(request, 'Curso editado com sucesso!')

			return redirect('app:course:manage')

	else:

		form = CourseForm(instance = course)
	
	context['form'] = form
	context['course'] = course

	return render(request, "course/update.html", context)

def view(request, slug):
	context = {}

	course = get_object_or_404(Course, slug = slug)

	context['course'] = course

	return render(request, "course/view.html", context)

def filter_cat(request, slug):
	context = {}

	category = get_object_or_404(Category, slug = slug)

	context['courses'] = Course.objects.filter(category = category)
	context['categories'] = Category.objects.all()
	context['cat'] = category

	return render(request, "course/filtered.html", context)

def index_cat(request):
	context = {
		'categories': Category.objects.all(),
	}

	return render(request, "category/index.html", context)

def create_cat(request):
	context = {}

	form = CategoryForm(request.POST or None)
	
	if form.is_valid():
		category = form.save(commit = False)
		category.slug = slugify(category.name)

		category.save()

		messages.success(request, 'Categoria criada com sucesso!')

		return redirect('app:course:manage_cat')
	
	context['form'] = form

	return render(request, "category/create.html", context)

def update_cat(request, slug):
	context = {}
	
	category = get_object_or_404(Category, slug = slug)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance = category)
	
		if form.is_valid():
			category = form.save(commit = False)
			category.slug = slugify(category.name)

			category.save()

			form = CategoryForm()

			messages.success(request, 'Categoria editada com sucesso!')

			return redirect('app:course:manage_cat')

	else:

		form = CategoryForm(instance = category)
	
	context['form'] = form

	return render(request, "category/update.html", context)

def view_cat(request, slug):
	context = {}

	category = get_object_or_404(Category, slug = slug)

	context['category'] = category

	return render(request, "category/view.html", context)

def index_modules(request, slug_course):
	context = {}

	course = get_object_or_404(Course, slug = slug_course)

	context['course'] = course
	context['modules'] = Module.objects.filter(course = course)

	return render(request, "module/index.html", context)

def create_modules(request, slug_course):
	context = {}

	course = get_object_or_404(Course, slug = slug_course)
	
	if request.method == 'POST':
		form = ModuleForm(request.POST)
	
		if form.is_valid():
			module = form.save(commit = False)
			module.slug = slugify(module.name)
			module.course = course

			module.save()

			messages.success(request, 'Módulo criado com sucesso!')

			return redirect('app:course:manage_mods', course.slug)

	else:

		form = ModuleForm({'course': course})
	
	context['form'] = form
	context['course'] = course

	return render(request, "module/create.html", context)

def update_modules(request, slug, slug_course):
	context = {}
	
	module = get_object_or_404(Module, slug = slug)

	if request.method == 'POST':
		form = ModuleForm(request.POST, instance = module)
	
		if form.is_valid():
			module = form.save(commit = False)
			module.slug = slugify(module.name)

			module.save()

			messages.success(request, 'Módulo editado com sucesso!')

			return redirect('app:course:manage_mods', slug_course)

	else:

		form = ModuleForm(instance = module)
	
	context['form'] = form
	context['course'] = module.course

	return render(request, "module/update.html", context)