# Generated by Django 3.1.8 on 2023-03-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_productos_cantventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='cantventas',
            field=models.PositiveIntegerField(auto_created=True, default=0, editable=False, verbose_name='Cantidad de ventas'),
        ),
    ]