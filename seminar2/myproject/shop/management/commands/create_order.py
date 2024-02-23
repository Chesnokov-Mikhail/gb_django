from django.core.management.base import BaseCommand
from shop.models import Product, Client, Order
from random import choices, choice

class Command(BaseCommand):
    help = "Create Order"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()
        for i in range(1,11):
            order_product = choices(products, k=i)
            order_price = 0
            for product in order_product:
                order_price += product.price
            order = Order.objects.create(client = choice(clients),
                                         total_price = order_price)
            for product in order_product:
                order.products.add(product)
            order.save()
            self.stdout.write(f'create {order}\n')