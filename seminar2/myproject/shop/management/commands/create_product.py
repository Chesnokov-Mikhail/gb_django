from django.core.management.base import BaseCommand
from shop.models import Product
from random import uniform, randint
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Product"

    def handle(self, *args, **kwargs):
        for i in range(1,31):
            product = Product(name = f'Product_{i}',
                                description = '. '.join(lorem_ipsum.paragraphs(2, common=False)),
                                price = round(uniform(1.00, 100000.00), 2),
                                quantity = randint(1,100),
                                add_date = f'2024-01-{randint(10,30)}')
            product.save()
            self.stdout.write(f'create {product}\n')