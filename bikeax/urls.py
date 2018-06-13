"""adminside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from ecom.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/$',dashboard, name="dashboard"),
    url(r'^dashboard/category/$',dashcategory, name="dashcategory"),
    url(r'^dashboard/product/$',dashproduct, name="dashproduct"),
    url(r'^dashboard/addcategory/$',addcategory, name="addcategory"),
    url(r'^dashboard/addproduct/$',addproduct, name="addproduct"),
    url(r'^dashboard/sales/$', salesreport, name="sales"),
    
    url(r'^$',index ,name="index"),
    url(r'^checkout$',checkout, name="checkout"),
    url(r'^category/(?P<pk>\d+)/', categoryview,name='category'),
    url(r'^search/',search,name="search"),
    url(r'^user_detail/',user_detail, name="user_detail"),
    url(r'^product/(?P<pk>\d+)/', product_detail, name='product_detail'),

    url(r'^cart/$', cart_detail, name='cart_detail'),
    url(r'^cart/add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    url(r'^cart/remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
    url(r'^CustomerDetail/',CustomerDetail,name="CustomerDetail"),    
    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
