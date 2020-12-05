class MyClass:
	
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


x = MyClass()
print(x.age)
