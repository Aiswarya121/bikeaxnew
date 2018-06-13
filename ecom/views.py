# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response, get_object_or_404, redirect
from .models import *
from .models import Product

from django.db.models import Q

from .cart import Cart
from .forms import CartAddProductForm

import re

from .forms import CategoryForm , ProductForm, CustomerDetailForm
from django.contrib.auth.decorators import user_passes_test

from django.views.decorators.http import require_POST


# Create your views here.
@user_passes_test(lambda u:u.is_superuser)
def dashboard(request):
    admin = request.user
    return render(request, "backend/index.html", {'admin':admin,})


def index(request):
    cart = Cart(request)
    categories=Category.objects.all()
    products=Product.objects.all()[:4]
    productstwo = Product.objects.all()[8:10]
    featured = Product.objects.all()[10:13]
    productsnext = Product.objects.all()[4:8]
    context = {
     'products':products,
     'productstwo':productstwo,
     'featured':featured,
     'productsnext':productsnext,
     'categories':categories,
     'cart':cart,
     }
    return render(request,'frontend/index.html', context)

def categoryview(request, pk):
	categories=Category.objects.all()
	category=Category.objects.get(pk=pk)
	products = Product.objects.filter(Categories = category)
	return render(request,'frontend/category.html', {'products':products, 'categories':categories })

def checkout(request):
	return render(request,'frontend/checkout.html')

def dashcategory(request):
	items=Category.objects.all()
	return render(request,'backend/category.html' ,{'items':items})

def dashproduct(request):
	items=Product.objects.all()
	return render(request,'backend/products.html' ,{'items':items})



def addcategory(request):
	form=CategoryForm()
	if request.method=="POST":
		form=CategoryForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
	return render(request,'backend/addcategory.html' ,{'form':form})


def addproduct(request):
	form=ProductForm()
	if request.method=="POST":
		form=ProductForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
	return render(request,'backend/addproduct.html',{'form':form})



#search box
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):

    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        print query_string
        entry_query = get_query(query_string, [ 'Name',])
        print entry_query

        found_entries = Product.objects.filter(entry_query)

    return render_to_response('frontend/search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          )


def product_detail(request, pk):
    post=get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request,'frontend/single.html', {'post': post, 'cart_product_form':CartAddProductForm})


def categoryview(request, pk):
    category=Category.objects.get(pk=pk)
    products = Product.objects.filter(Categories = category)
    return render(request,'frontend/category.html', {'products':products })



def user_detail(request):
    users= User.objects.all()
    return render(request,'backend/user_detail.html',{'users':users})


def salesreport(request):
    users= User.objects.all()
    return render(request,'backend/salesreport.html',{'users':users})





@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'frontend/detail.html', {'cart': cart})

def CustomerDetail(request):
    form=CustomerDetailForm()
    if request.method=="POST":
        form=CustomerDetailForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()             
    return render(request,'frontend/CustomerDetail.html',{'form':form})