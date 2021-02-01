from __future__ import print_function
from main import PizzaShop
from employee2 import PIzzaRobot, Server

class Customer:
    def __init__(self, _name):
        self._name = _name

    def order(self, server):
        print(self._name, "orders from ", server)

    def pay(self, server):
        print(self._name, "pays for item to ", server)

class oven:
    def bake(self):
        print('oven bakes')

class PIzzaShop:
    def __init__(self):
        self.server = Server('Ahmed')
        self.chef = PizzaRobot('Ali')
        self.oven = Oven()
    
    def order(self, _name):
        customer = Customer(_name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
        
if __name__ == "__main__":
    scene = PizzaShop()
    scene.order('Homer')
    print()
    scene.order('Ahmed')