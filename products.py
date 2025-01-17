from promotions import Promotion

class Product():
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError("Quantity must be a non-negative number")
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.active = False
        self._promotion = None

    @property
    def promotion(self):
        return self._promotion
    
    @promotion.setter
    def promotion(self, promotion):
        if self._promotion is not None:
            raise ValueError("Product already has a promotion")
        if promotion is not None and not isinstance(promotion, Promotion):
            raise ValueError("Promotion must be of type Promotion")
        self._promotion = promotion
        
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
        promotion_str = f" {self._promotion}" if self._promotion else ""
        return f"{self.name} Quantity:{self.quantity}{promotion_str}"
    
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        # Then check if we have enough stock
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")
        
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        if self._promotion:
            final_price = self._promotion.apply_promotion(self, quantity)
        else:
            final_price = quantity * self.price
            
        return final_price

    def set_promotion(self, promotion):
        self.promotion = promotion






class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price
        
    def show(self):
        return f"{self.name}"





class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
        
    def buy(self, quantity):
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} units at a time")
        return super().buy(quantity)
        
    def show(self):
        return f"{self.name}, Max quantity: {self.maximum}"
      

