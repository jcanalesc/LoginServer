from django.db import models

# Create your models here.

class User(models.Model):
	sM = "M"
	sF = "F"
	SEX_CHOICES = (
		(sM, "Masculino"),
		(sF, "Femenino"),
	)
	rut 	= models.CharField("Rut del usuario", 		max_length=20, primary_key=True)
	nombre 	= models.CharField("Nombre del usuario", 	max_length=50) 
	apellido= models.CharField("Apellido del usuario",	max_length=50) 
	foto	= models.ImageField("Foto de perfil",	upload_to="userpics")
	email	= models.EmailField("Direccion de email del usuario", max_length=254)
	edad	= models.IntegerField("Edad del usuario")
	sexo	= models.CharField("Sexo del usuario", choices=SEX_CHOICES, default="M", max_length=2)

	def __unicode__(self):
		return "(%s) %s %s" % (self.rut, self.apellido, self.nombre)

