# Generated by Django 3.1.8 on 2023-03-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20230319_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='cantventas',
            field=models.PositiveIntegerField(auto_created=True, default=0, editable=False, verbose_name='Sales Quantity'),
        ),
    ]