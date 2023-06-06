import braintree
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

gateway = braintree.BraintreeGateway(   #ovo iz nekog razloga radi i nasao sam postavku na internetu
            braintree.Configuration.configure(
            environment=braintree.Environment.Sandbox,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY))

#gateway=braintree.BraintreeGateway(settings.BRAINTREE_CONF) # ovo iz nekog razloga ne radi mada je po knjizi
#===============================================================================================================
# pokusavam da namesti da ukoliko neko nece da plati karticom da moze da stampa fakturu i da je plati virmanski

#def stampajII_pdf(request, order_id):
 #   order= get_object_or_404(Order, id=order_id)
 #   return render (request,
  #                 'pdf.html',
   #                 {'order':order})
# =============================================================================================================


def payment_process(request):
    order_id=request.session.get('order_id')
    order= get_object_or_404(Order, id=order_id)
    total_cost= order.get_total_cost()

    if request.method=='POST':
        nonce=request.POST.get('payment_method_nonce', None)
        result=gateway.transaction.sale({'amount':f'{total_cost:.2f}',
                                         'payment_method_nonce':nonce,
                                         'options':{'submit_for_settlment':True}})
        if result.is_success:
            order.paid=True
            order.braintree_id=result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        #client_token = gateway.client_token.generate()# ovo je po knjizi
        client_token = braintree.ClientToken.generate()
        return render (request,
                        'process.html',
                        {'order':order,
                        'client_token':client_token })

def payment_done(request):
    return render(request, 'done.html')

def payment_canceled(request):
    return render(request, 'canceled.html')