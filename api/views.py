from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import get_collection
from django.conf import settings


def search(request):
    collection = get_collection(settings.GARMENT_COLLECTION)
    searchQuery = request.GET.get('q', '')
    per_page = 20
    page = int(request.GET.get('p', '1'))
    offset = (page - 1) * per_page
    neededFields = {'image_urls': 1, 'product_title': 1, 'url': 1,
                    'product_description': 1, 'currency_code': 1, 'price': 1}
    if searchQuery == '':
        total = collection.count_documents({})
        results = collection.find({}, neededFields).skip(
            offset).limit(per_page)
    else:
        queryDic = {'product_title':  {'$regex': searchQuery, '$options': 'i'}}
        total = collection.count_documents(queryDic)
        results = collection.find(queryDic, neededFields).skip(
            offset).limit(per_page)
    resultsList = []
    for row in results:
        del row['_id']
        resultsList.append(row)
    results = {
        'data': resultsList,
        'page': page,
        'per_page': per_page,
        'count': len(resultsList),
        'total': total
    }
    return JsonResponse(results)
