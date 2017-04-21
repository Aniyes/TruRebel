from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404

# Create your views here.


def collection_view(request):

    name = request.user
    product = get_object_or_404(Product)
    template = "Products.html"
    context = {
        'object': product,
        'username': name,
        'message': 'Hello'

    }

    return render(request, template, context)


def detail_view(request, object_id=None):

    name = request.user
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        'object': product,
        'username': name,
        'message': 'Hello'

    }

    return render(request, template, context)



def list_view(request):
    product = Product.objects.all()
    template = "list_view.html"
    context = {
        "product": product,
    }

    return render(request, template, context)

#def register(request):

