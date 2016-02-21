from django.shortcuts import render, Http404
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.base  import ContextMixin
from products.models import Category
from shopcart.models import Cart
from shoporder.models import Order
from shoporder.forms import FormOrder
from django.http import JsonResponse

class OrderD(View):

	def get_context_data(self, **kwargs):
		context = super(Rorder, self).get_context_data(**kwargs)
		context['menu12'] = Category.objects.all()
		print context
		return context

	def get(self, request, *args, **kwargs):
		self.context = {'menu':Category.objects.all(), 'form':FormOrder, 'real':False}
		return render(request, 'real.html', self.context)	

	def post(self, request, *args, **kwargs):
		f = FormOrder(request.POST)
		if f.is_valid():
			o = Order()
			o.cart = Cart.objects.get(id=request.session['cart_id'])
			o.name = 'Vasa'
			o.email = 'Vasa@list.ru'
			o.save()
			return render(request, 'real.html', {'real':True, 'message':'!!!!'}) 	
		return render(request, 'real.html', {'form':FormOrder,'real':False}) 	


class OrderAjax(View):

	def get(self, request, *args, **kwargs):
		print 'rrr'
		context = {'menu':Category.objects.all()}
		return render(request, '404.html', context)	

	def post(self, request, *args, **kwargs):
		f = FormOrder(request.POST or None)
		if request.is_ajax():
			if f.is_valid():
				o = Order()
				o.cart = Cart.objects.get(id=request.session['cart_id'])
				o.name = f.cleaned_data['name']
				o.email = f.cleaned_data['email']
				o.save()
				del request.session['cart_id']
				return JsonResponse({'success':True,'email':f.cleaned_data['email']})	
			else:
				return JsonResponse({'success':False})	
		else:
			raise Http404	


class Rorder(TemplateView):
	template_name = 'real.html'

	def get_context_data(self, **kwargs):
		context = super(Rorder, self).get_context_data(**kwargs)
		context['menu'] = Category.objects.all()
		print context
		return context

class FOrder(FormView):
	template_name = 'form.html'
	form_class = FormOrder
	success_url = '/shoporder/thanks/'

	def form_valid(self, form):
		print form
		return super(FOrder, self).form_valid(form)

