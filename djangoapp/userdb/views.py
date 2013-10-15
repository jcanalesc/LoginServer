# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.core.files import File


from userdb.models import User
from random import randint
from datetime import datetime
import os




def sync(request):
	response = None
	try:
		site_path = os.path.abspath(os.path.dirname(__file__))
		print site_path
		jsonobj = simplejson.loads(request.POST.get('jsondata',''))
		print "Received objects: %d" % (len(jsonobj))
		for item in jsonobj:
			imgnewurl = "userpics/" + datetime.now().strftime("%Y%m%d%H%M%S") + "_%d.png" % (randint(10,99))
			outputimg = File(open(site_path + imgnewurl, "wb"))
			print "abri el archivo"
			outputimg.write(item["foto"].decode("base64"))
			outputimg.close()
			del item["foto"]
			del item["ts"]
			item["foto"] = imgnewurl
			item["edad"] = int(item["edad"])
			u = User(**item)
			u.save()
		response = HttpResponse('{"success": true}', content_type="application/json")
		return response
	except Exception as e:
		response = HttpResponse('{"success": false, "error": "'+str(e)+'"}', content_type="application/json")
		return response