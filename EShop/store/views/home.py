from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from ..models import Product
from ..models import Category
from ..models import Customer
from django.views import View
# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    catID = request.GET.get("category")
    if catID:
        products = Product.get_prod_by_catagory(catID)
    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories
    return render(request, "index.html", data)