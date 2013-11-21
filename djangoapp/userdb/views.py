# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.core.files import File


from userdb.models import User
from random import randint
from datetime import datetime
import os
import StringIO



def sync(request):
	response = None
	try:
		site_path = "/root/media/"
		#print site_path
		jsonobj = simplejson.loads(request.POST.get('jsondata',''))
		print "Received objects: %d" % (len(jsonobj))
		for item in jsonobj:
			imgnewurl = "userpics/" + datetime.now().strftime("%Y%m%d%H%M%S") + "_%d.png" % (randint(10,99))
			outputimg = File(open(os.path.join(site_path,imgnewurl), "wb"))
			outputimg.write(item["foto"].decode("base64"))
			outputimg.close()
			del item["foto"]
			del item["ts"]
			item["foto"] = imgnewurl
			item["edad"] = datetime.strptime(item["edad"], "%Y-%m-%d")
			u = User(**item)
			u.save()
		response = HttpResponse('{"success": true}', content_type="application/json")
		return response
	except Exception as e:
		response = HttpResponse('{"success": false, "error": "'+str(e)+'"}', content_type="application/json")
		return response

def getExcel(request):
	import xlwt

	ss = StringIO.StringIO()

	wb = xlwt.Workbook()
	sheet = wb.add_sheet("Usuarios")
	sheet.write(0, 0, "Rut")
	sheet.write(0, 1, "Nombre")
	sheet.write(0, 2, "Apellido")
	sheet.write(0, 3, "Email")
	sheet.write(0, 4, "Fecha de nacimiento")
	sheet.write(0, 5, "Sexo")
	sheet.write(0, 6, "Direccion")
	sheet.write(0, 7, "Comuna")
	sheet.write(0, 8, "Preferencia 1")
	sheet.write(0, 9, "Preferencia 2")
	sheet.write(0, 10, "Preferencia 3")
	for ix, usr in enumerate(User.objects.all()):
		sheet.write(ix+1, 0, usr.rut)
		sheet.write(ix+1, 1, usr.nombre)
		sheet.write(ix+1, 2, usr.apellido)
		sheet.write(ix+1, 3, usr.email)
		sheet.write(ix+1, 4, usr.edad.strftime("%Y-%m-%d"), xlwt.easyxf("", "YYYY/MM/DD"))
		sheet.write(ix+1, 5, usr.sexo)
		sheet.write(ix+1, 6, usr.direccion)
		sheet.write(ix+1, 7, usr.comuna)
		sheet.write(ix+1, 8, usr.pref1)
		sheet.write(ix+1, 9, usr.pref2)
		sheet.write(ix+1, 10, usr.pref3)
	
	wb.save(ss)

	bindata = ss.getvalue()
	ss.close()
	response = HttpResponse(bindata)
	response["Content-Description"] = "File Transfer"
	#response["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
	response["Content-Type"] = "application/vnd.ms-excel"
	response["Content-Disposition"] = "attachment; filename='userdb.xls'"
	response["Content-Transfer-Encoding"] = "binary"
	response["Expires"] = 0
	response["Cache-Control"] = "must-revalidate"
	response["Pragma"] = "public"
	response["Content-Length"] = len(bindata)

	return response

