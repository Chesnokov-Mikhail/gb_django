from django.core.management.base import BaseCommand
from shop.models import Client
from random import choices
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Client"

    def handle(self, *args, **kwargs):
        tel_numbers = list(range(10))
        for i in range(1,11):
            client = Client(name=f'Name_{i}',
                            email=f'mail_{i}@torn.com',
                            telephone=f'+7{"".join(map(str,choices(tel_numbers, k=10)))}',
                            address=lorem_ipsum.words(5,common=False))
            client.save()
            self.stdout.write(f'create {client}\n')