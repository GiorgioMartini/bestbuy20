from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, product, discount):
        self.product = product
        self.discount = discount

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass
        

# return product.price * quantity * self.discount

class PercentDiscount(Promotion):
    def __init__(self, product, percent):
        super().__init__(product, percent)
        self.name = "name"
    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent)



class SecondHalfPrice(Promotion):
    def __init__(self, product):
        super().__init__(product, 0.5)
        self.discounted_price = 0
        self.name = "name"

    def apply_promotion(self, product, quantity):
        if quantity > 1:
            for i in range(quantity):
                # Even numbered items (0-based index) are 50% off
                if i % 2 == 0:
                    self.discounted_price += product.price/2      
                else:
                    self.discounted_price += product.price
        return self.discounted_price



class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name, 0)
        self.name = name

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        charged_items = quantity - free_items
        return charged_items * product.price
