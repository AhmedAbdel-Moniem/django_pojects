class Person:
    
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def del_name(self):
        del self._name
    
    name = property(get_name, set_name, del_name, "my made documentation")


ahmed = Person('Bob Smith')
ahmed = Person('Ahmed')
print(ahmed.name)
ahmed.name = 'Mohamed'
print(ahmed.name)
# del ahmed.name
print(Person.name.__doc__)


