from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import KontrolaHardware

def kontrola_listview(request):
	template_name = 'Kontrola/kontrola_list.html',
	queryset = KontrolaHardware.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)
