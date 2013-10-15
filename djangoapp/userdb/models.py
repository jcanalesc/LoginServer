from django.db import models

# Create your models here.

class User(models.Model):
	sM = "M"
	sF = "F"
	dVodka 		= "vodka"
	dWhisky 	= "whisky"
	dPisco		= "pisco"
	dRon 		= "ron"
	dCerveza	= "cerveza"
	dVino		= "vino"
	dTequila	= "tequila"

	SEX_CHOICES = (
		(sM, "Masculino"),
		(sF, "Femenino"),
	)
	DRINK_CHOICES = (
		(dVodka, "Vodka"),
		(dWhisky, "Whisky"),
		(dPisco, "Pisco"),
		(dRon, "Ron"),
		(dCerveza, "Cerveza"),
		(dVino, "Vino"),
		(dTequila, "Tequila"),
	)
	rut 	= models.CharField("Rut del usuario", 		max_length=20, primary_key=True)
	nombre 	= models.CharField("Nombre del usuario", 	max_length=50) 
	apellido= models.CharField("Apellido del usuario",	max_length=50) 
	foto	= models.ImageField("Foto de perfil",	upload_to="userpics")
	email	= models.EmailField("Direccion de email del usuario", max_length=254)
	edad	= models.DateField("Fecha de nacimiento del usuario")
	sexo	= models.CharField("Sexo del usuario", choices=SEX_CHOICES, default=sM, max_length=2)
	direccion = models.CharField("Direccion del usuario", max_length=200)
	pref1	= models.CharField("Preferencia de trago 1", choices=DRINK_CHOICES, default=dVodka, max_length=15)
	pref2	= models.CharField("Preferencia de trago 2", choices=DRINK_CHOICES, default=dVodka, max_length=15)
	pref3	= models.CharField("Preferencia de trago 2", choices=DRINK_CHOICES, default=dVodka, max_length=15)


	def __unicode__(self):
		return "(%s) %s %s" % (self.rut, self.apellido, self.nombre)

