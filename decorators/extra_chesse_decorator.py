from interfaces.pizza import Pizza

class ExtraCheeseDecorator(Pizza):
    def __init__(self, base_pizza: Pizza):
        self.base_pizza = base_pizza

    def get_name(self):
        return self.base_pizza.name + " with Extra Cheese"
    
    def get_toppings(self):
        base_toppings = self.base_pizza.get_toppings()
        base_toppings.append("Extra Cheese")
        
        return base_toppings