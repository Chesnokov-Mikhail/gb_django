from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telephone']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имени (name)'
    readonly_fields = ['registration_date']
    fieldsets = [
                    (
                        'Основная информация',
                        {
                            'fields': ['name', 'email', 'telephone', 'registration_date'],
                        },
                    ),
                    (
                        'Адрес',
                        {
                            'classes': ['collapse'],
                            'fields': ['address'],
                        }
                    ),
                ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']
    ordering = ['name', 'price', 'quantity']
    list_filter = ['add_date', 'price', 'quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описания (description)'
    fieldsets = [
        (
            'Основная информация',
            {
                'fields': ['name', 'price', 'quantity', 'add_date'],
            },
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'fields': ['description', 'image'],
            }
        ),
    ]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['client','products', 'total_price', 'order_date']
    list_display = ['get_client', 'get_products', 'total_price', 'order_date']
    list_filter = ['total_price', 'order_date']
    search_fields = ['get_client']
    search_help_text = 'Поиск по полю Клиенту (client)'
    readonly_fields = ['order_date']

    def get_products(self, obj):
        return "\n".join([p.name for p in obj.products.all()])

    def get_client(self, obj):
        return "\n".join([obj.client.name])
