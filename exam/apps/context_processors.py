from exam.apps.questions.models import profile
import django

def user_avatar(request):
	try:
		avatar = None
		user = request.user
		up = profile.objects.get(nickname=user)
		avatar = "/media/%s"%up.avatar
	except:
		avatar = "/static/images/photo.jpg"
	return avatar


def my_processor(request):
	context = {"django_version":django.get_version(),
	           "get_avatar_profile":user_avatar(request),
	}
	return context
