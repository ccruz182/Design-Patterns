from interfaces.pizza import Pizza

from pizzas.hawaiian_pizza import HawaiianPizza
from pizzas.meat_pizza import MeatPizza
from pizzas.pepperoni_pizza import PepperoniPizza

from decorators.extra_chesse_decorator import ExtraCheeseDecorator

def order(pizza: Pizza):
    print("You have ordered a {} pizza. The toppings are {}".format(pizza.get_name(), pizza.get_toppings()))


order(ExtraCheeseDecorator(HawaiianPizza()))
order(HawaiianPizza())
order(MeatPizza())