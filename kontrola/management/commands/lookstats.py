import request
from django.core.management import BaseCommand


class Command(BaseCommand):
	help = "Request for stats hardware"

	def handle(self, *args, **options):
		r = request.get(http://0.0.0.0:5000/cpu)