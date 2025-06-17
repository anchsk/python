class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')


apple = FruitFlavour()

""" 
when you initialize the child class, you don’t initialize the base class with it. 
super() function helps you to achieve this and add the initialization of base class with the derived class.
"""
