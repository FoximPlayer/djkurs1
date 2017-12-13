import requests
from django.core.management import BaseCommand
import pprint

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument('cpu', nargs='+', type=str),
		parser.add_argument('memory', nargs='+', type=str),
	
	def handle(self, *args, **options):
		if options['cpu']:
			pr = requests.get("http://localhost:5000/cpu")
			cpu = {}
			if pr.status_code == requests.codes.ok:
				pp = pprint.PrettyPrinter(indent = 1)
				cpu = pr.json()
			pp.pprint(cpu)

		elif options['memory']:
			mem = requests.get("http://localhost:5000/mem")
			memory = {}
			if mem.status_code == requests.codes.ok:
				pp = pprint.PrettyPrinter(indent = 2)
				memory = mem.json()
			pp.pprint(memory)
        
        
    