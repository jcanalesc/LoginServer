# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.utils import simplejson

from appmanager.models import User

def index(request):
	return HttpResponse("Hello, world.")


def auth(request):
	username = request.GET.get('user','')
	passwd	 = request.GET.get('pass', '')
	response_data = { "success": False }
	try:
		uo = User.objects.get(pk=username)
		if uo.password == passwd:
			# login succesful, send app_id
			response_data = {
				'appid': uo.app.id,
				'host':	 uo.app.host,
				'success': True
			}
		else:
			response_data = {
				'success': False
			}
	except:
		pass
	finally:
		return HttpResponse(simplejson.dumps(response_data), content_type="application/json")



