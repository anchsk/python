price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# {:.2f} formats a float to 2 decimal places
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# 7.5 8.175

"{0:.0f}".format(10.5)
# '10' integrer value
"{:.2f}".format(0.5)
# '0.50' for floats
"{:.2s}".format('Python')
# 'Py' for strings
"{:<6s}".format("Py")
# 'Py    ' left aligned
"{:>6s}".format("Py")
# '    Py' right aligned
"{:^6s}".format("Py")
# '  Py  ' center aligned


