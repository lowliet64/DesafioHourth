from .consts import SEED_OBJECTS
from django.core.management.base import BaseCommand
from ...models import Product
import datetime

def populate_products():
    for seed in SEED_OBJECTS:
        product = Product(product_url=seed.get('product_url'),product_url_created_at=seed.get('product_url__created_at'),consult_date=seed.get('consult_date'),c=seed.get('c'))
        product.save()


class Command(BaseCommand):
  def handle(self, *args, **options):
    populate_products()
    # clear_data()
    print("completed")