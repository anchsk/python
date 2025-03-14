class Apple:
    def __init__(self): # dunder method
        self.color = "red"
        self.flavor = "sweet"


# Create an instance of a class
honeycrisp = Apple()
print(honeycrisp.color)
# red

class Apple_2:
    """ Documentation for the function Apple_2 """
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
    def function_name(a):
        """ Documentationi for the function_name """
        print(a)


# Modify variables
fuji = Apple_2("red", "tart")
print(fuji.flavor)
# sweet

print(Apple)
# <class '__main__.Apple'>
print(honeycrisp)
# <__main__.Apple object at 0x10ee822d0>

print(Apple_2)
# <class '__main__.Apple_2'>
print(fuji)
# an apple which is red and tart

# help(Apple_2)

print(Apple_2.__doc__)
print(Apple_2.function_name.__doc__)


