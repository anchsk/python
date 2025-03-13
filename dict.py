my_dict = {'a': 10, 'b': 20, 'c': 30}
for item in my_dict:
    print(item)
# a b c
for item in my_dict:
    print(my_dict[item])
# 10 20 30

for (item, value) in my_dict.items(): # <<< items!
    print("{} is {}".format(item,value))

# a is 10
# b is 20
# c is 30

print(my_dict.keys())
# dict_keys(['a', 'b', 'c'])
print(my_dict.values())
# dict_values([10, 20, 30])


print(my_dict)
# {'a': 10, 'b': 20, 'c': 30}
print(my_dict.items())
# dict_items([(a,10), ('b', 20), ('c', 30)])
a = tuple(my_dict.items())
print(a)
# (('a', 10), ('b', 20), ('c', 30))
b = list(my_dict.items())
print(b)
# [('a', 10), ('b', 20), ('c', 30)]
c = str(my_dict.items())
print(c)
# dict_items([('a', 10), ('b', 20), ('c', 30)])
print(type(c)) 
# <class 'str'>

if "a" in my_dict:
    print('is in')

if "x" not in my_dict:
    print('is not')