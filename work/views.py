from django.shortcuts import render
from .models import Content, Product, Indent, Business, Payment, Newclient, Oldclient, PaymentFollow, QuotationFollow, Billing
from project_and_purchase.models import Stock


def home(request):
    return render(request, 'work/home.html')

def quotation(request):
    content= Content.objects.all()
    products = Product.objects.all()
    stock = Stock.objects.all()
    param= {'person':content, 'product':products, 'stock':stock}
    if request.method=="POST":
        name = request.POST.get('name', '')
        atten = request.POST.get('atten', '')
        contact = request.POST.get('contact', '')
        state = request.POST.get('state', '')
        statecode = request.POST.get('statecode', '')
        address = request.POST.get('address', '')
        subject = request.POST.get('subject', '')
        quotnum = request.POST.get('quotnum', '')
        quotdate = request.POST.get('quotdate', '')
        prodname = request.POST.get('prodname', '')
        qty = request.POST.get('quantity', '')
        unit = request.POST.get('unit', '')
        rate = request.POST.get('rate', '')
        tax = request.POST.get('tax', '')
        signature = request.POST.get('signature', '')

        quotation= Content(name=name, atten=atten, contact=contact,
        state=state, statecode=statecode, address=address, subject=subject, quotnum=quotnum, quotdate=quotdate,)
        prod = Product(prodname=prodname, qty=qty, unit=unit,
                       rate=rate, tax=tax, signature=signature)

        prod.save()
        quotation.save()

    return render(request, 'work/quotation.html', param)

def work_report(request):
    content = Content.objects.all()
    newclient = Newclient.objects.all()
    oldclient= Oldclient.objects.all()
    quotfollow = QuotationFollow.objects.all()
    payFollow = PaymentFollow.objects.all()
    param = {'quotation':content, 'oldclient':oldclient, 'newclient': newclient, 'quotfollow':quotfollow, 'payFollow': payFollow}

    if request.method=="POST":
        client_name = request.POST.get('client_name', '')
        clientname= request.POST.get('clientname', '')
        clients = request.POST.get('clients', '')
        grahak = request.POST.get('grahak', '')
        purpose = request.POST.get('purpose', '')
        purposetalk = request.POST.get('purposetalk', '')
        contact_person =  request.POST.get('contact_person', '')
        contactperson = request.POST.get('contactperson', '')
        contactprson = request.POST.get('contactprson', '')
        contact_no = request.POST.get('contact_no','')
        contactno = request.POST.get('contactno', '')
        contactnumber = request.POST.get('contactnumber', '')
        reverted = request.POST.get('reverted', '')
        reply = request.POST.get('reply', '')
        reverts = request.POST.get('reverts', '')
        revert = request.POST.get('revert', '')
        quotnumber = request.POST.get('quotnumber', '')
        qtnumber = request.POST.get('qtnumber', '')
        sentdate = request.POST.get('sentdate', '')
        followupdate =  request.POST.get('followupdate', '')
        dueamt = request.POST.get('dueamt', '')
        new= Newclient(client_name=client_name, purpose=purpose, contact_person=contact_person, contact_no=contact_no, reverted=reverted)
        new.save()
        old = Oldclient(clientname=clientname, purposetalk=purposetalk, contactperson=contactperson, contactno=contactno, revert=revert)
        old.save()
        followpay= PaymentFollow(clients=clients, quotnumber=quotnumber, sentdate=sentdate, followupdate=followupdate, reply=reply, dueamt=dueamt)
        followpay.save()
        followquot =  QuotationFollow(grahak=grahak, qtnumber=qtnumber, contactprson=contactprson, contactnumber=contactnumber, reverts=reverts)
        followquot.save()
    return render(request, 'work/work_report.html', param)

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
        make = request.POST.get('make', '')
        deadline = request.POST.get('deadline', '')
        indent= Indent(product=product, quantity=quantity, unit=unit, required=required, refer=refer, priority=priority, make=make,deadline = deadline)
        indent.save()
    return render(request, 'work/indent.html', param)

def businesstarget(request):
    business_target = Business.objects.all()
    param = {'business': business_target}
    if request.method=="POST":
        client = request.POST.get('client', '')
        quot = request.POST.get('quot', '')
        sent = request.POST.get('sent', '')
        follow = request.POST.get('follow', '')
        status = request.POST.get('status', '')
        week = request.POST.get('week', '')
        business= Business(client=client, quot=quot,sent=sent,follow=follow,status=status, week=week)
        business.save()


    return render(request, 'work/targets.html', param)

def paymenttarget(request):
    payment = Payment.objects.all()
    
    if request.method=="POST":
        client_name = request.POST.get('client_name', '')
        due = request.POST.get('due', '')
        bill_no = request.POST.get('bill_no', '')
        amount = request.POST.get('amount', '')
        followup = request.POST.get('followup', '')
        stat = request.POST.get('stat', '')
        recieve = request.POST.get('recieve', '')
        weekno = request.POST.get('weekno','')

        paying = Payment(client_name=client_name, due=due, bill_no=bill_no, amount=amount,followup=followup, stat=stat,recieve=recieve, weekno=weekno)
        paying.save()

    a= due
    b= amount
    c = recieve  
    total = int(a) + int(b)- int(c)
    param = {'pay': payment, 'total':total}
    return render(request,'work/payment.html', param)


def clients(request):
    return render(request, 'work/clients.html')

def stock(request):
    stock = Stock.objects.all()
    param = {'item': stock}
    return render(request, 'work/stock.html', param)

def billing(request):
    bills = Billing.objects.all()
    param = {'bills':bills}
    if request.method=="POST":
        branch = request.POST.get('branch', '')
        client_gst = request.POST.get('client_gst', '')
        client_state = request.POST.get('client_state','')
        company = request.POST.get('company', '')
        company_add = request.POST.get('company_add', '')
        bill_date = request.POST.get('bill_date', '')
        rgpdate = request.POST.get('rgpdate', '')
        rgpno = request.POST.get('rgpno','')
        po_no = request.POST.get('po_no', '')
        po_date = request.POST.get('po_date', '')
        hsn = request.POST.get('hsn', '')
        item_description = request.POST.get('item_description', '')
        quantity_item = request.POST.get('quantity_item', '')
        pricing = request.POST.get('pricing','')
        total = request.POST.get('total', '')
        gst = request.POST.get('gst', '')

        bill = Billing(branch=branch, client_gst = client_gst, client_state=client_state,company=company,company_add=company_add,bill_date=bill_date, rgpdate=rgpdate,
                rgpno=rgpno, po_no=po_no, po_date=po_date, hsn=hsn, item_description = item_description, quantity_item = quantity_item, pricing = pricing, total=total, gst = gst)
        bill.save()

    return render(request, 'work/billing.html', param)


# Create your views here.
