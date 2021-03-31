from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=20)
    atten = models.CharField(max_length=20)
    contact = models.IntegerField()
    state = models.CharField(max_length=15)
    statecode = models.CharField(max_length=3)
    address = models.CharField(max_length=80)
    subject = models.CharField(max_length=30)
    quotnum = models.CharField(max_length=20)
    quotdate = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    prodname = models.CharField(max_length=100)
    qty= models.CharField(max_length=5)
    unit = models.CharField(max_length=5)
    rate= models.IntegerField()
    tax= models.CharField(max_length=5)
    signature= models.CharField(max_length=20)

    def __str__(self):
        return self.prodname

class Indent(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)
    unit = models.CharField(max_length=8)
    required= models.CharField(max_length=50)
    refer= models.CharField(max_length=20)
    status = models.CharField(max_length=10, default='', editable=False)
    priority = models.CharField(max_length=10, default='', editable=True)
    make = models.CharField(max_length=10, default='', editable=True)
    deadline = models.CharField(max_length=30, default='', editable=True)

    def __str__(self):
        return self.product

class Business(models.Model):
    client= models.CharField(max_length=50)
    quot= models.CharField(max_length=50)
    sent = models.CharField(max_length=20)
    follow= models.CharField(max_length=20)
    status= models.CharField(max_length=100)
    week = models.CharField(max_length=10,default='',editable=True)

    def __str__(self):
        return self.client

class Payment(models.Model):
    client_name= models.CharField(max_length=50)
    due = models.IntegerField()
    bill_no= models.IntegerField()
    amount = models.IntegerField()
    followup= models.CharField(max_length=20)
    stat = models.CharField(max_length=100)
    recieve= models.IntegerField()
    weekno = models.CharField(max_length=10, default='', editable=True)

    def __str__(self):
        return self.client_name

class Newclient(models.Model):
    client_name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    reverted = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name

class Oldclient(models.Model):
    clientname = models.CharField(max_length=50)
    purposetalk = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=20)
    contactno = models.CharField(max_length=10)
    revert = models.CharField(max_length=50)

    def __str__(self):
        return self.clientname

class PaymentFollow(models.Model):
    clients = models.CharField(max_length=50)
    quotnumber = models.CharField(max_length=50)
    sentdate = models.CharField(max_length=20)
    followupdate = models.CharField(max_length=20)
    reply = models.CharField(max_length=50)
    dueamt = models.CharField(max_length=10, default='', editable=True)
    total_balance = models.CharField(max_length=10, default='', editable=True)

    def __str__(self):
        return self.clients

class QuotationFollow(models.Model):
    grahak = models.CharField(max_length=50)
    qtnumber = models.CharField(max_length=50)
    contactprson = models.CharField(max_length=20)
    contactnumber = models.CharField(max_length=10)
    reverts = models.CharField(max_length=50)

    def __str__(self):
        return self.grahak


class Billing(models.Model):
    branch = models.CharField(max_length=10)
    client_gst = models.CharField(max_length=20)
    client_state = models.CharField(max_length=10)
    company = models.CharField(max_length=30)
    company_add = models.CharField(max_length=50)
    bill_date =  models.CharField(max_length=10)
    rgpdate = models.CharField(max_length=10)
    rgpno =models.CharField(max_length=20)
    po_no = models.CharField(max_length=20)
    po_date = models.CharField(max_length=10, default='', editable=True)
    hsn = models.CharField(max_length=10)
    item_description = models.CharField(max_length=100)
    quantity_item = models.CharField(max_length=10)
    pricing = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    gst =models.CharField(max_length=10)

    def __str__(self):
        return self.company

# Create your models here.
