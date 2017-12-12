from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import KontrolaHardware

def kontrola_listview(request):
	template_name = 'Kontrola/kontrolahardware_list.html',
	queryset = KontrolaHardware.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class KontrolaListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = KontrolaHardware.objects.filter(
					Q(producent__iexact=slug) | 
					Q(producent__iconatains=slug)
				)
		else:
			queryset = KontrolaHardware.objects.all()
		return queryset

class KontrolaDetailView(DetailView):
	queryset = KontrolaHardware.objects.all()

	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(KontrolaDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

