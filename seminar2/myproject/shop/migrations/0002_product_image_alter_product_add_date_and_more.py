# Generated by Django 4.1 on 2024-03-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
