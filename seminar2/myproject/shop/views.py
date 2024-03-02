from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import View
from datetime import datetime, timedelta
from .models import Client, Product, Order
from .forms import AddProduct, AddImageProduct,EditProduct, SelectProduct

# Create your views here.

class PostProduct(View):
    def get(self,request):
        form = AddProduct()
        title_content = 'Добавление товара'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        return render(request, 'shop/add_product.html', context)

    def post(self,request):
        form = AddProduct(request.POST, request.FILES)
        title_content = 'Добавление товара'
        message = 'Товар не сохранен'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        if form.is_valid():
            product = Product(name=form.cleaned_data['name'],
                                description=form.cleaned_data['description'],
                                price=form.cleaned_data['price'],
                                quantity=form.cleaned_data['quantity'],
                                add_date=form.cleaned_data['add_date'],
                                image=form.cleaned_data['image'])
            product.save()
            message = 'Изображение товара сохранено'
        context['message'] = message
        return render(request, 'shop/add_image_product.html', context)

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
        title_content = 'Добавление изображение товара'
        message = 'Изображение товара не сохранено'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs_name = fs.save(image.name, image)
            Product.objects.filter(pk=form.cleaned_data['product'].pk).update(image=fs_name)
            message = 'Изображение товара сохранено'
        context['message'] = message
        return render(request, 'shop/add_image_product.html', context)

class SelectEditProduct(View):
    def get(self,request):
        form = SelectProduct()
        title_content = 'Выбрать товар для редактирования'
        context = {'title': 'Интернет-магазин',
                       'content': {'title': title_content,
                                   },
                       'form_select': form,
                       }
        return render(request, 'shop/edit_product.html', context)

    def post(self,request):
        form = SelectProduct(request.POST)
        if form.is_valid():
            return redirect('post_edit_product', form.cleaned_data['product'].pk)

class PostEditProduct(View):
    def get(self,request, product_id):
        if product_id:
            product_select = Product.objects.filter(pk=product_id).first()
            if product_select:
                form_edit = EditProduct(initial={'product_id': product_select.pk,
                                                'name':product_select.name,
                                                'description':product_select.description,
                                                'price':product_select.price,
                                                'quantity':product_select.quantity,
                                                'add_date':product_select.add_date,
                                                'image':product_select.image,
                                                 }
                                        )
                # form = SelectProduct(initial={'product':product_select})
                title_content = 'Редактировать выбранный товар'
                context = {'title': 'Интернет-магазин',
                           'content': {'title': title_content,
                                       },
                           # 'form_select': form,
                           'form_edit': form_edit,
                           }
        else:
            return redirect('post_edit_product')
        return render(request, 'shop/edit_product.html', context)

    def post(self,request, product_id):
        form_edit = EditProduct(request.POST, request.FILES)
        message = 'Товар не изменен'
        print(form_edit.is_valid())
        if form_edit.is_valid():
            image = form_edit.cleaned_data['image']
            fs = FileSystemStorage()
            fs_name = fs.save(image.name, image)
            data = form_edit.cleaned_data
            Product.objects.filter(pk=product_id).update(name=data['name'],
                                                                    description=data['description'],
                                                                    price=data['price'],
                                                                    quantity=data['quantity'],
                                                                    add_date=data['add_date'],
                                                                    image=fs_name, )
            message = 'Товар изменен'
        title_content = 'Редактирование товара'
        context = {'title': 'Интернет-магазин',
                   'content': {'title': title_content,
                               },
                   'form_edit': form_edit,
                   }
        context['message'] = message
        return render(request, 'shop/edit_product.html', context)

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