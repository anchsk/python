def example(num):
    return num * 2

arr = map(example, range(0,10))
print(arr) 
# <map object at 0x1004bc250>
print(list(arr))