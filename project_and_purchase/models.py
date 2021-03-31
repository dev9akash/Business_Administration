from django.db import models


class Stock(models.Model):
	item_name = models.CharField(max_length=50)
	item_desc = models.CharField(max_length=200)
	item_qty = models.CharField(max_length=10)
	item_image = models.ImageField(upload_to='static/stock', default="")
	hsn = models.CharField(max_length=6, default='', editable=True)
	purchase_rate = models.CharField(max_length=10, default='', editable=True)
	unit = models.CharField(max_length=10, default='', editable=True)
	receiveddate = models.CharField(max_length=10, default='', editable=True)
	purchasedby = models.CharField(max_length=10, default='', editable=True)

	def __str__(self):
		return self.item_name


class SentInvoice(models.Model):
	invoice_id = models.AutoField(primary_key=True)
	buyer = models.CharField(max_length=30)
	location = models.CharField(max_length=50)
	issuedate = models.DateField()
	po_no = models.CharField(max_length=20)
	item = models.CharField(max_length=200)
	amount = models.IntegerField()
	quantity = models.IntegerField()
	unit = models.CharField(max_length=5)
	purpose = models.CharField(max_length=20)





# Create your models here.
