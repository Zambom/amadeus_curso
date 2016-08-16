from django.contrib.auth.decorators import login_required
from .models import Subscribe

@login_required
def subscribed_courses(request):
	return {
		'subscribed_courses': Subscribe.objects.filter(user = request.user)[:3] or None
	}