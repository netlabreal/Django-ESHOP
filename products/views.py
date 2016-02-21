from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View

from products.models import *
from shopcart.models import *
from django.utils import timezone
from django.http import JsonResponse
import json


class ProdList(ListView):
    model = Products
    template_name = 'plist.html'

    def get_context_data(self, **kwargs):
        context = super(ProdList, self).get_context_data(**kwargs)
        context['menu'] = Category.objects.all()
        print context
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.args[0])
        return Products.objects.filter(category=self.category)
   


class ProdDetail(DetailView):
    model = Products
    template_name = 'pdetail.html'

    def get_context_data(self, **kwargs):
        context = super(ProdDetail, self).get_context_data(**kwargs)
        context['menu'] = Category.objects.all()
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    object = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['menu'] = Category.objects.all()
        return context


def main(request):
    cts = Category.objects.all()
    pr = Products.objects.all().order_by("?")[:6]
    context={
        "menu" : cts,
        "recomend" : pr
    }
    return render_to_response('f.html', context)


def prod_detail(request, pid):
    return HttpResponse('s1 '+str(pid))


class Count(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            cid = request.session.get('cart_id')
            if cid is not None:
                cart = Cart.objects.get(id=cid)
                kol = Citem.objects.filter(cart=cart).count()
            else:
                kol=0    
            return JsonResponse({'count':kol})
        else:
            raise Http404
