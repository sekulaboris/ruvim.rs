from celery import shared_task # instalirana je celery 5 verzija u django

from Ruvim_site.celery import app  #ovo je za novije verzije celerija ja koristim 4.2.2.
from django.core.mail import send_mail
from .models import Order



@shared_task()
def order_created(order_id):
    order= Order.objects.get(id=order_id)
    subject= f'Order nr. {order.id}'
    message= f'Dear { order.first_name },\n\n'\
             f'You have successfully placed an order.'\
             f'Your order ID is { order.id }.'
    mail_sent= send_mail(subject, 
                        message, 
                        'sekulaboris@yahoo.com', 
                        [order.email])
    return mail_sent


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()