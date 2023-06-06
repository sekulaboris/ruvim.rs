from decimal import Decimal
from django.conf import settings
from OnlineShop.models import Product

class Cart(object):

    def __init__(self, request):
        self.session= request.session
        cart= self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart= self.session[settings.CART_SESSION_ID]={}
        self.cart= cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]= {'quantity': 0,
                                    'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id= str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        pdv=Decimal(1.20)
        pdv_pdv=Decimal(0.20)
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)

        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['pdv']=Decimal(item['price']* item['quantity'] * pdv_pdv)
            item['osnovica']= Decimal (item['price']* item['quantity'])
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        pdv=Decimal(1.20)
        return sum(Decimal(item['price'])* item['quantity'] * pdv for item                    
                    in self.cart.values())
              

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
        