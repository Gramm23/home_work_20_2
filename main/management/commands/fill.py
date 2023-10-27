import json

from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-8') as data_file:
            categories = json.load(data_file)
            categories_list = []
            for category in categories:
                categories_list.append(
                    Category(category['pk'], **category['fields'])
                )

            Category.objects.bulk_create(categories_list)
