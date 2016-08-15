from django import template
import datetime

register = template.Library()

@register.filter(expects_localtime=True)
def valid_period(course):
	actual = datetime.date.today()

	return  course.init_register_date <= actual <= course.end_register_date