from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
#ovo je test ne uspevam da uradim dovoljno dobro da mi u stampaj racun ucita Order bazu podataka -------------------------------------
#=========================================== pokusavam da ukoliko neko nece da plati karticom da uplatu odstampa i uplati je virmanski
@staff_member_required
def stampaj_pdf(request, order_id):
    order= get_object_or_404(Order, id=order_id)
    return render (request,
                   'pdf.html',
                    {'order':order})
#=====================================================================================================

#ovde je kraj testa ----------------------------------------

@staff_member_required
def admin_order_pdf(request, order_id):
    order=get_object_or_404(Order, id=order_id)
    html=render_to_string('pdf.html',
                         {'order': order})
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    return response

# Create your views here.
 
@staff_member_required
def admin_order_detail(request, order_id):
    order= get_object_or_404(Order, id=order_id)
    cart=Cart(request)
    return render (request,
                   'orders_detail.html',
                    {'order':order,
                    'cart':cart})

def order_create(request):
    cart= Cart(request)
    if request.method == 'POST':
        form= OrderCreateForm(request.POST)
        if form.is_valid():
            order= form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        osnovica=item['osnovica'],
                                        pdv=item['pdv'],
                                        quantity= item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id']=order.id
            #return redirect (reverse('payment:process')) #ovo mi koristi kada bude bilo osposobljeno za placanje preko kartice.abs()
            return render(request,
                            'created.html',
                            {'order':order})

    else:
        form= OrderCreateForm()
    return render(request,
                  'create.html',
                  {'cart': cart,
                  'form': form})






