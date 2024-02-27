from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Client, Product, Order

# Create your views here.

class GetIndex(View):
    def get(self, request):
        products = Product.objects.all()
        title_content = 'Список товаров:'
        context = {'title': 'Интернет-магазин',
                    'content': {'title': title_content,
                                'result': products,
                                }
                    }
        return render(request, 'shop/index.html', context)

class GetProduct(View):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        title_content = f'Описание продукта: {product.name}'
        context = {'title': 'Интернет-магазин / продукт',
                    'content': {'title': title_content,
                                'result': product,
                                }
                    }
        return render(request, 'shop/product.html', context)

class GetAllOrderClient(View):
    def get(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        orders = Order.objects.filter(client=client).order_by('order_date').all()
        result = {}
        for order in orders:
            products = Product.objects.filter(pk=order.products).all()
        title_content = f'Список заказов пользователя: {client.name}'
        context = {'title': 'Интернет-магазин / пользователь',
                    'content': {'title': title_content,
                                'result': orders,
                                }
                    }
        return render(request, 'shop/client_orders.html', context)