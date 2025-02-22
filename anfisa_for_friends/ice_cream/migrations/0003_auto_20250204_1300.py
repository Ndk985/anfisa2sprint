# Generated by Django 3.2.16 on 2025-02-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20250203_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'объект «Обёртка»', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинги'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]
