print('hello', 'you', sep="-")
print("hi there", end="\n")
name1 = ""
# name1 = input("Enter your name: ")
print(name1)

print(10==10) # True
print(10 == 10.00) # True
print(10 == '10') # False
print(10 == int('10')) # True

user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = float(user_num_1) + float(user_num_2)
print(user_sum)

n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + str(float(n1)) + " and " + str(float(n2)) + " is " + str(user_sum))