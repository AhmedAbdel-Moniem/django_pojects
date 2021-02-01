from __future__ import print_function
from employees import PizzaRobot


class Employee:
    def __init__(self, _name, salary=0):
        self._name   = _name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self._name, 'does stuff')

    def __repr__(self):
        return "<Employee: _name=%s, salary= %s>" % (self._name, self.salary)


class Chef(Employee):
    def __init__(self, _name):
        Employee.__init__(self, _name, 1000)

    def work(self):
        print(self._name, "makes food")


class Server(Employee):
    def __init__(self, _name):
        Employee.__init__(self, _name, 2000)

    def work(self):
        print(self._name, 'interfaces with customers')


class PIzzaRobot(Chef):
    def __init__(self, _name):
        Chef.__init__(self, _name)

    def work(self):
        print(self._name, 'makes pizza')


if __name__ == "__main__":
    bob = PIzzaRobot('bob')
    print(bob)
    bob.giveRaise(.1)
    print(bob)
    print()
    for klass in Employee, Server, Chef, PizzaRobot:
        obj = klass(klass.__name__)
        print(obj)