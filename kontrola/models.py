from django.db import models

# Create your models here.
class KontrolaHardware(models.Model):
	podzespol 	= models.CharField(max_length = 120)
	producent 	= models.CharField(max_length = 120, null = True, blank = True)
	timestamp 	= models.DateTimeField(auto_now_add = True)
	update 		= models.DateTimeField(auto_now = True)
	slug 		= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.podzespol

	@property
	def podzespol(self):
		return self.podzespol
