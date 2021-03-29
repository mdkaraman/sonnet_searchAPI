from django.core.management.base import BaseCommand

from sonnets.models import Sonnet

class Command(BaseCommand):
    
    def load_sonnets(self):
        # Open file containing sonnets
        with open('1041.txt') as f:
            lines = f.readlines() 
            f.close()

        # Isolate lines containing sonnets
        sonnet_lines = [line.strip() for line in lines[43:2661]]

        # Group sonnets in list of lists
        sonnets = []
        for i in range(0, len(sonnet_lines), 17):
            sonnets += [sonnet_lines[i:i+17]]

        # Remove all empty strings
        sonnets = [[line for line in sonnet if line] for sonnet in sonnets]

        for sonnet in sonnets:
            sonnet = Sonnet(number=sonnet[0], text=sonnet[1:])
            sonnet.save()

    def handle(self, *args, **options):
            self.load_sonnets()
