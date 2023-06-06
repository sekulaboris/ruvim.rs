from django.db import models
from OnlineShop.models import Product
from cart.cart import Cart



class Order(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    company= models.CharField(max_length=50)
    m_broj= models.CharField(max_length=8)
    pib= models.CharField(max_length=9)
    email= models.EmailField()
    address= models.CharField(max_length=250)
    postal_code= models.CharField(max_length=20)
    city= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    paid= models.BooleanField(default=False)
    braintree_id=models.CharField(max_length=150, blank=True)


    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost (self):
        return sum((item.get_cost())+(item.get_p)  for item in self.items.all ())

    


   

class OrderItem (models.Model):
    order= models.ForeignKey(Order, 
                            related_name='items', 
                            on_delete=models.CASCADE)
    product= models.ForeignKey(Product, 
                            related_name= 'order_items', 
                            on_delete= models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    pdv=models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.PositiveIntegerField()
    osnovica=models.DecimalField(max_digits=10, decimal_places=2)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    p=models.DecimalField(max_digits=10, decimal_places=2, default=.20)

    

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity 

    
    def get_osnova (self):
        return self.price * self.quantity

    def get_pp (self):
        return self.price * self.quantity * self.p
    
    



