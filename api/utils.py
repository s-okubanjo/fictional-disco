from pymongo import MongoClient
from django.conf import settings


def get_db_handle():
    client = MongoClient(host=settings.DB_HOST,
                         port=int(settings.DB_PORT),
                         username=settings.DB_USERNAME,
                         password=settings.DB_PASSWORD
                         )
    return client[settings.DB_NAME]


def get_collection(name):
    return get_db_handle()[name]
