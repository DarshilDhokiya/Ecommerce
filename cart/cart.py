from myapp.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            self.session.modified =True
    def __len__(self):
        return len(self.cart)
    def get_prods(self):
        product_ids = self.cart.keys()  # Get product IDs from the cart dictionary
        products = Product.objects.filter(id__in=product_ids)  # Use id__in to filter by IDs
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self,product,quntity):
        product_id=str(product)
        product_qty = int(quntity)
        oucart = self.cart
        oucart[product_id]= product_qty

        self.session.modified = True
        thing = self.cart
        return thing
    def delete(self,product):
        product_id=str(product)

        if product_id in self.cart:
            del self.cart[product_id]


        self.session.modified = True
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0

        for key, value in quantities.items():
            key = int(key)
            product_id = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)

        return total
