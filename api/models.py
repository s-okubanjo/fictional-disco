from .utils import get_collection
from django.conf import settings


def search_product_title(query, offset, limit):
    collection = get_collection(settings.GARMENT_COLLECTION)
    neededFields = {'image_urls': 1, 'product_title': 1, 'url': 1,
                    'product_description': 1, 'currency_code': 1, 'price': 1}
    total = collection.count_documents(query)
    results = collection.find(query, neededFields).skip(
        offset).limit(limit)
    return total, results
