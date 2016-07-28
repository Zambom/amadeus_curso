import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField('Login', max_length = 35, unique = True, validators = [
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um nome de usuário válido. '
				'Este valor deve conter apenas letras, números '
				'e os caracteres: @/./+/-/_ .'
				, 'invalid'
			)
		], help_text = 'Um nome curto que será usado para identificá-lo de forma única na plataforma e também para acessá-la')
	email = models.EmailField('E-mail', unique = True)
	name = models.CharField('Nome', max_length = 100, blank = True)
	city = models.CharField('Cidade', max_length = 90, blank = True)
	state = models.CharField('Estado', max_length = 30, blank = True)
	gender = models.CharField('Sexo', max_length = 1, choices = (('M', 'Masculino'), ('F', 'Feminino')))
	image = models.ImageField(verbose_name = 'Imagem', blank = True, upload_to = 'users/', default = 'no_image.jpg')
	birth_date = models.DateField('Data de Nascimento', null = True, blank = True)
	phone = models.CharField('Telefone', max_length = 30, blank = True)
	cpf = models.CharField('Cpf', max_length = 15, blank = True)
	type_profile = models.IntegerField('Tipo', null = True, blank = True, choices = ((1, 'Professor'), (2, 'Aluno')))
	date_created = models.DateTimeField('Data de Cadastro', auto_now_add = True)
	is_staff = models.BooleanField('Administrador', default = False)
	is_active = models.BooleanField('Ativo', default = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

	def __str__(self):
		return self.name or self.username

	def det_full_name(self):
		return str(self)

	def get_short_name(self):
		return str(self).split(" ")[0]