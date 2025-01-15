class Product():
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.active = False
        
    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity
    
    def is_active(self):
        return self.active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def show(self):
        return f"{self.name} ({self.quantity})"
    
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        # Then check if we have enough stock
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")
        
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        
        self.name = name
        self.price = price 
        self.active = False
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        
    def show(self):
        return f"{self.name})"        

class LimitedProduct(Product):
    def __init__(self, name, price, quantity,  maximum):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        
        self.name = name
        self.price = price 
        self.active = False
        self.maximum = maximum
        
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        
        if quantity > self.maximum:
            raise ValueError("Not enough quantity in stock")
        
    def show(self):
        return f"{self.name}, Max quantity: {self.maximum})"        
      

