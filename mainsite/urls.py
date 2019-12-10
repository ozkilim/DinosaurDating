from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
	path('', views.landing, name='landing'),
	path('events', views.events, name='events'),
	path('reserve', views.reserve, name='reserve'),
	path('references', views.references, name='references'),
	path('tickets/<int:id>', views.tickets, name='tickets'),
	path(r'^pay/(?P<charge>\w+?)/$', views.pay.as_view(), name='pay'),
	path('charge/', views.charge, name='charge'),

]