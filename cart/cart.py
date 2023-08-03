from products.models import product

class Cart:
    
    def __init__(self, request):
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = dict()

        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1,add_or_replace=False):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0}
        if add_or_replace:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self,product):
        product_id=str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            
        self.save()
            
    def __iter__(self):
        product_ids=self.cart.keys()
        
        products=product.objects.filter(id__in=product_ids)
        
        cart=self.cart.copy()
        
        for product1 in products:
            cart[str(product1.id)]['product_object']= product1
            
        for item in cart.values():
            item['total_price']=item['quantity']*item['product_object'].price
            yield item
    
    def __len__(self):
        return len(self.cart.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()
        
    def get_total_price(self):
        product_ids=self.cart.keys()
        
        products=product.objects.filter(id__in=product_ids)
        
        return sum(item['quantity']*item['product_object'].price for item in self.cart.values())