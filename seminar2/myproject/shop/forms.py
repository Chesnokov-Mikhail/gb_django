from django import forms
from django.forms.widgets import ClearableFileInput
import datetime
from .models import Product

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = 'Изменить изображение'
    clear_checkbox_label = 'Удалить изображение'

class AddImageProduct(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(), label='Выберите товар', to_field_name="id")
    image = forms.ImageField(label='Загрузите изображение товара')

class AddProduct(forms.Form):
    name = forms.CharField(max_length=200, label='Наименование товара')
    description = forms.CharField(required=False, widget=forms.Textarea(), label='Описание товара')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена товара')
    quantity = forms.IntegerField(initial=0, label='Количество товара')
    add_date = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'type':'date'}), label='Дата добавления товара')
    image = forms.ImageField(label='Изображение товара')

class EditProduct(forms.Form):
    # product_id = forms.IntegerField(required=False, disabled=True, label='ID товара')
    name = forms.CharField(max_length=200, label='Наименование товара')
    description = forms.CharField(required=False, widget=forms.Textarea(), label='Описание товара')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена товара')
    quantity = forms.IntegerField(initial=0, label='Количество товара')
    add_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'type': 'date'}),
                               label='Дата добавления товара')
    image = forms.ImageField(label='Изображение товара', widget=MyClearableFileInput)

class SelectProduct(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(), label='Выберите товар')