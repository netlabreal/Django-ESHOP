from products import views
from django.conf import settings

"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls')),
    url(r'^category/$', views.CategoryList.as_view(), name='catalog'),
    url(r'^category/([\w-]+)/$', views.ProdList.as_view(), name='catalogs'),
    url(r'^shopcart/', include('shopcart.urls')),
    url(r'^shoporder/', include('shoporder.urls')),
    url(r'^shopcart_count/$',views.Count.as_view(), name='cart_count'),
    url(r'^$', views.main, name='home'),

 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True}),    
 url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True}),    
]
