from .models import Subscribe

def subscribed_courses(request):
	return {
		'subscribed_courses': Subscribe.objects.filter(user = request.user)[:3]
	}