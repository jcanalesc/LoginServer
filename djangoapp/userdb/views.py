# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from userdb.models import User
from random import randint
def sync(request):
	jsonobj = simplejson.loads(request.POST.get('jsondata',''))
	for item in jsonobj:
		imgnewurl = "userpics/" + datetime.now().strftime("%Y%m%d%H%M%S") + "_%d.png" % (randint(10,99))
		outputimg = open(imgnewurl, "wb")
		outputimg.write(item["foto"].decode("base64"))
		outputimg.close()
	return HttpResponse('{"success": true}', content_type="application/json")