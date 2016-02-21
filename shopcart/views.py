from django.shortcuts import render_to_response, get_object_or_404, render
from products.models import *
from shopcart.models import *
from shoporder.forms import FormOrder
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json


class CartView(SingleObjectMixin, View):
    model = Cart

    def get_object(self, *args, **kwargs):
        self.request.session.set_expiry(0)
        c_id = self.request.session.get('cart_id')
        if c_id is None:
            cart = Cart()
            cart.save()
            c_id = cart.id
            self.request.session['cart_id'] = c_id
        cart = Cart.objects.get(id=c_id)
        if self.request.user.is_authenticated():
            cart.user = self.request.user
            cart.save()
        return cart

    def get(self, request, *args, **kwargs):
        cts = Category.objects.all()
        if request.is_ajax():
            cart = self.get_object()
            item_id = request.GET.get('item')

            delete = request.GET.get('delete', False)
            if item_id:
                ins = get_object_or_404(Products, id=item_id)
                c_item, created = Citem.objects.get_or_create(cart=cart, item=ins)
                ret = c_item.item.title
                kol = request.GET.get('kol')
                if kol:
                    if int(kol) > 0:
                        c_item.kol = int(kol)
                        c_item.save()
                if delete:
                    c_item.delete()
                total = c_item.total
                cart = self.get_object()
                itog = cart.itog
                count = cart.kol_items()

                return JsonResponse({"item": ret, "item_added": created, "item_deleted": delete, "kol":count,"total":total, "itog":itog})
        else:
            context = {'form':FormOrder,"menu": cts, 'object': self.get_object()}
            return render(request, 'shopcart.html', context)


def ajax(request):
    if request.is_ajax:
        item = request.GET.get('item')
        kol = request.GET.get('kol')
        delete = request.GET.get('del')
        if request.GET.get('item'):
            cts = Category.objects.all()
            for item in cts.values():
                print type(item)
                #tt.update({'title': item.title})
            #r = [dict(item) for item in cts.values()]
            #return HttpResponse(json.dumps(r))
            #results = [ob for ob in cts]
            #for k in results:
            #    print k.get_category_url()
            #return JsonResponse(r)
        return JsonResponse({"success": True}, {"success": False})
