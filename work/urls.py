from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('quotation/', views.quotation, name='quotation'),
    path('work_report', views.work_report, name='report'),
    path('indent/', views.indent, name='indent'),
    path('clients/', views.clients, name='clients'),
    path('businesstarget/', views.businesstarget, name='businesstarget'),
    path('paymenttarget/', views.paymenttarget, name='paymenttarget'),
    path('stock/', views.stock, name='stockitem'),
    path('billing/', views.billing, name='billing')

]