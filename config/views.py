from django.views import View
from django.shortcuts import render


class Index(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)
    
class About(View):
    def get(self, request):
        context = {}
        return render(request, 'about.html', context)

class Blog_details(View):
    def get(self, request):
        context = {}
        return render(request, 'blog-details.html', context)

class Blog(View):
    def get(self, request):
        context = {}
        return render(request, 'blog.html', context)
    
class Checkout(View):
    def get(self, request):
        context = {}
        return render(request, 'checkout.html', context)
    
class Contact(View):
    def get(self, request):
        context = {}
        return render(request, 'contact.html', context)

class Shop_details(View):
    def get(self, request):
        context = {}
        return render(request, 'shop-details.html', context)

class Shop(View):
    def get(self, request):
        context = {}
        return render(request, 'shop.html', context)

class Shopping_cart(View):
    def get(self, request):
        context = {}
        return render(request, 'shopping-cart.html', context)


