from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import search_product_title


def search(request):
    searchQuery = request.GET.get('q', '')
    per_page = 20
    page = int(request.GET.get('p', '1'))
    offset = (page - 1) * per_page
    if searchQuery == '':
        total, results = search_product_title({}, offset, per_page)
    else:
        queryDic = {'product_title':  {'$regex': searchQuery, '$options': 'i'}}
        total, results = search_product_title(queryDic, offset, per_page)
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
