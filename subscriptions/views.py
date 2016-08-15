from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from .forms import SubscribeForm
from .models import Subscribe

@login_required
def subscribe(request):
	if request.method == 'POST':
		print(request.POST)
		form = SubscribeForm(request.POST)

		print(form)

		if form.is_valid():
			form.save()

			messages.success(request, _('Course subscribed successfully!'))

			return redirect('app:course:manage')

class Index(LoginRequiredMixin, generic.ListView):

	login_url = '/'
	redirect_field_name = 'next'
	template_name = 'subscribed/index.html'
	context_object_name = 'subscriptions'
	paginate_by = 10

	def get_queryset(self):
		return Subscribe.objects.filter(user = self.request.user)