from django.core.management.base import BaseCommand
from shop.models import Product, Client, Order
from random import choices, choice

class Command(BaseCommand):
    help = "Search all order by client name"

    def add_arguments(self, parser):
        parser.add_argument('name_client', type=str, help='Name client')

    def handle(self, *args, **kwargs):
        name_client = kwargs['name_client']
        orders = Order.objects.filter(client__name__icontains=name_client).all()
        self.stdout.write(f'{orders}')