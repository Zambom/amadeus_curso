from django.db import models

class Category(models.Model):

	name = models.CharField('Nome', max_length = 100, unique = True)
	slug = models.SlugField('Identificador', max_length = 100)
	create_date = models.DateField('Criação', auto_now_add = True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return self.name

class Course(models.Model):

	name = models.CharField('Nome', max_length = 100, unique = True)
	slug = models.SlugField('Identificador', max_length = 100)
	objectivies = models.TextField('Objetivos', blank = True)
	content = models.TextField('Conteúdo', blank = True)
	max_students = models.PositiveIntegerField('Máximo de Alunos', blank = True)
	create_date = models.DateField('Criação', auto_now_add = True)
	init_register_date = models.DateField('Data de Cadastro (Início)')
	end_register_date = models.DateField('Data de Cadastro (Final)')
	init_date = models.DateField('Data de Início do Curso')
	end_date = models.DateField('Data de Final do Curso')
	image = models.ImageField(verbose_name = 'Imagem', blank = True, upload_to = 'courses/', default = 'no_image.jpg')
	category = models.ForeignKey(Category, verbose_name = 'Categoria', default = 1)

	class Meta:

		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

	def __str__(self):
		return self.name

class Module(models.Model):

	name = models.CharField('Nome', max_length = 100)
	slug = models.SlugField('Identificador', max_length = 100)
	description = models.TextField('Descrição', blank = True)
	visible = models.BooleanField('Visível', default = True, blank = True)
	create_date = models.DateField('Criação', auto_now_add = True)
	course = models.ForeignKey(Course, verbose_name = 'Curso')

	class Meta:

		verbose_name = 'Módulo'
		verbose_name_plural = 'Módulos'

	def __str__(self):
		return self.name