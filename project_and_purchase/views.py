from django.shortcuts import render
from work.models import Indent, Billing
from .models import Stock

def home(request):
    return render(request, 'project/home.html')
# Create your views here.

def stock(request):
    items = Stock.objects.all()
    param = {'item': items}
    return render(request, 'project/stock.html', param)

def indent(request):
    content = Indent.objects.all()
    param = {'data': content}
    if request.method=="POST":
        product = request.POST.get('product', '')
        quantity = request.POST.get('quantity', '')
        unit = request.POST.get('unit', '')
        required = request.POST.get('required', '')
        refer = request.POST.get('refer', '')
        priority = request.POST.get('priority', '')
        indent= Indent(product=product, quantity=quantity, unit=unit, required=required, refer=refer, priority=priority)
        indent.save()
    return render(request, 'project/indent.html', param)

def billing(request):
    bills = Billing.objects.all()
    param = {'bills':bills}
    return render(request, 'project/billing.html', param)