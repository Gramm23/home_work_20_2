import json

from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('product.json', 'r', encoding='utf-8') as data_file:
            products = json.load(data_file)
            for product in products:
                category_id = product['fields']['category']
                category = Category.objects.get(product_name=category_id)
                product_instance = Product(
                    product_name=product['fields']['product_name'],
                    description=product['fields']['description'],
                    category=category,
                    unit_price=product['fields']['unit_price'],
                    image=product['fields']['image']
                )
                product_instance.save()
