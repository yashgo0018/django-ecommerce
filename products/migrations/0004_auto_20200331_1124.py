# Generated by Django 3.0.4 on 2020-03-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200331_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='tag_list', to='products.Product'),
        ),
    ]