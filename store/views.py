from django.http import JsonResponse
from .firebase import db

def list_products(request):
    products_ref = db.collection('products')
    docs = products_ref.stream()

    products = []
    for doc in docs:
        product = doc.to_dict()
        product['id'] = doc.id
        products.append(product)

    return JsonResponse(products, safe=False)
