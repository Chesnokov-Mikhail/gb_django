from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views import View
from datetime import datetime, timedelta
from .models import Client, Product, Order
from .forms import AddProduct, AddImageProduct

# Create your views here.

class PostImageProduct(View):
    def get(self,request):
        form = AddImageProduct()
        title_content = 'Добавление изображение товара'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        return render(request, 'shop/add_image_product.html', context)

    def post(self,request):
        form = AddImageProduct(request.POST, request.FILES)
        message = 'Изображение товара не сохранено'
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(image=image)
            product.save()
            message = 'Изображение товара сохранено'
        title_content = 'Добавление изображение товара'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        return render(request, 'shop/add_image_product.html', context)

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
        title_content = f'Описание товара: {product.name}'
        context = {'title': 'Интернет-магазин / товар',
                    'content': {'title': title_content,
                                'result': product,
                                }
                    }
        return render(request, 'shop/product.html', context)

class GetClients(View):
    def get(self, request):
        clients = Client.objects.all()
        title_content = f'Список клиентов:'
        context = {'title': 'Интернет-магазин / товар',
                    'content': {'title': title_content,
                                'result': clients,
                                }
                    }
        return render(request, 'shop/clients.html', context)

class GetAllOrderClient(View):
    def get(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        orders = Order.objects.filter(client=client).order_by('order_date').all()
        result = {}
        for order in orders:
            products = order.products.all()
            result[order] = products
        title_content = f'Список заказов клиента: {client.name}'
        context = {'title': 'Интернет-магазин / клиент',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'shop/client_orders.html', context)

class GetAllProductsByOrdersClient(View):
    def get(self, request, client_id):
        today = datetime.now()
        delta_list = [timedelta(days=7), timedelta(days=30), timedelta(days=365)]
        result = dict()
        client = Client.objects.get(pk=client_id)
        # Вариант вывода не отсортированных товаров (Товары не повторяются) по дате заказа, которые данные товары содержали
        # for delta in delta_list:
        #     orders = Order.objects.filter(client=client, order_date__gte=(today - delta)).all()
        #     result[delta] = set()
        #     for order in orders:
        #         products = order.products.all()
        #         result[delta].update(products)

        # Вариант вывода отсортированных товаров (Товары не повторяются) по дате заказа, которые данные товары содержали
        for delta in delta_list:
            orders = Order.objects.filter(client=client, order_date__gte=(today - delta)).order_by('-order_date').all()
            result[delta] = []
            product_set = set()
            for order in orders:
                products = order.products.all()
                for prod in products:
                    if prod not in product_set:
                        result[delta].append(prod)
                product_set.update(products)

        title_content = f'Список заказанных товаров клиента: {client.name}'
        context = {'title': 'Интернет-магазин / клиент',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'shop/client_products_orders.html', context)