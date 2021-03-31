from django.contrib import admin
from .models import Stock, SentInvoice

# Register your models here.
admin.site.register(Stock)
admin.site.register(SentInvoice)