from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, telephone: {self.telephone}, ' \
               f'address: {self.address}, registration_date: {self.registration_date}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    add_date = models.DateField()

    def __str__(self):
        return f'Productname: {self.name}, description: {self.description},' \
                f'price: {self.price}, quantity: {self.quantity}, add_date: {self.add_date}'

class Order(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        products = [product.name for product in self.products.all()]
        return f'Order_client: {self.client.name}, products: {products} total_price: {self.total_price}, order_date: {self.order_date}'