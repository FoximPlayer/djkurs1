from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class KontrolaHardware(models.Model):
	podzespol 	= models.CharField(max_length = 120)
	producent 	= models.CharField(max_length = 120, null = True, blank = True)
	timestamp 	= models.DateTimeField(auto_now_add = True)
	update 		= models.DateTimeField(auto_now = True)
	slug 		= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.podzespol

def hd_pre_save_receiver(sender, instance, *args, **kwargs):
	print('Saving...')
	print(instance.timestamp)

def hd_post_save_receiver(sender, instance, created, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()

pre_save.connect(hd_pre_save_receiver, sender = KontrolaHardware)

post_save.connect(hd_post_save_receiver, sender = KontrolaHardware)