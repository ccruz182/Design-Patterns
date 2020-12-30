from interfaces.pizza import Pizza

class MeatPizza(Pizza):
    def __init__(self):
        self.name = "Hawaiian"
        self.toppings = ["Cheese", "Tomato", "Meat"]
    
    def get_name(self):
        return self.name
    
    def get_toppings(self):
        return self.toppings