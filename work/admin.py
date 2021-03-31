from django.contrib import admin
from .models import Content, Product, Indent, Business, Payment, Newclient, Oldclient, PaymentFollow, QuotationFollow, Billing

admin.site.register(Content)
admin.site.register(Product)
admin.site.register(Indent)
admin.site.register(Business)
admin.site.register(Payment)
admin.site.register(Newclient)
admin.site.register(Oldclient)
admin.site.register(PaymentFollow)
admin.site.register(QuotationFollow)
admin.site.register(Billing)
# Register your models here.
