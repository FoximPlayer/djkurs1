from django.db import models

# Create your models here.
class KontrolaHardware(models.Model):
	podzespół 	= models.CharField(max_length = 120)
	producent 		= models.CharField(max_length = 120, null = True, blank = True)
	timestemp 	= models.DateTimeField(auto_now_add = True)
	update 		= models.DateTimeField(auto_now = True)
	slug 		= models.SlugField(unique = True)

	def __str__(self):
		return self.podzespół

	@property
	def title(self):
		return self.name
