num_1 = input("Enter the number:\n")
num_2 = input("Enter another number:\n")


""" try:
    print(sum(num_1 + num_2))
except:
    print("error!")
else: 
    print('the end')
     """
### another

while True:
    try:
        x = input("Number 1: ")
        x = int(x)
        if x == 'q':
            break

        y = input("Number 2: ")
        y = int(y)
        if y == 'q':
            break
    except ValueError:
       # print('Sorry need a number')
       pass
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}")
        
