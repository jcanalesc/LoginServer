from django.db import models
from django import forms

# Create your models here.

class App(models.Model):
	name = models.CharField('Nombre de la aplicacion', max_length=100)
	host = models.URLField('URL del host donde esta alojado el software monitor')
	def __unicode__(self):
		return "%s (%s)" % (self.name, self.host)


class User(models.Model):
	name	 = models.CharField('Nombre', max_length=150)
	username = models.CharField('Nombre de usuario para login', max_length=100, primary_key=True)
	# TODO: crear un PasswordField o algo asi
	password = models.CharField('Clave', max_length=128)
	active	 = models.BooleanField('Usuario Activo')
	app = models.ForeignKey(App)
	def __unicode__(self):
		return "%s - Activo: %s" % (self.name, "Si" if self.active else "No")


