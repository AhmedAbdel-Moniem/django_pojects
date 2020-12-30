class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    @ staticmethod
    def printNumInstance():
        print(Spam.numInstance)

a = Spam()
b = Spam()
c = Spam()
d = Spam()

Spam.printNumInstance()
c.printNumInstance()