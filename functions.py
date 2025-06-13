names = ['Alice', 'Jane', 'Caroline']

def reverse(str):
    return str[::-1]

reversed_names = map(reverse, names)

for x in reversed_names:
    print(x)