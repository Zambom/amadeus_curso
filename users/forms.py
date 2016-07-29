# coding=utf-8

from django import forms

from .models import User


class ProfileForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'birth_date', 'city', 'state', 'gender', 'type_profile', 'cpf', 'phone', 'image']

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'birth_date', 'city', 'state', 'gender', 'type_profile', 'cpf', 'phone', 'image', 'is_staff', 'is_active']