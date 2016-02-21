from shoporder import views
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [

    #url(r'^$', views.Order.as_view(), name='order'),
    url(r'^$', views.OrderD.as_view(), name='order'),
    url(r'^order/$', views.OrderAjax.as_view(), name='orderajax'),
    url(r'^form/$', views.FOrder.as_view(), name='forder'),

]
