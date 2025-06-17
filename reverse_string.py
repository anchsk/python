my_str = 'I love Japan'

new_str = []
for i, char in enumerate(my_str):
    new_str.insert(0,char)
# print(('').join(new_str))
      
      
# print(my_str[::-1]) # reverse a string

# str[start::stop:step]
print(my_str[::-3])

def string_reverse(str):
    if len(str) == 0:
        print('0!', str)
        return str
    else:
        print('str[0]:', str[0])
        new_str = string_reverse(str[1:]) + str[0]
        print(new_str)
        return new_str

# print(string_reverse(my_str))

""" 
0! 
n
na
nap
napa
napaJ
napaJ 
napaJ e
napaJ ev
napaJ evo
napaJ evol
napaJ evol 
napaJ evol I
napaJ evol I
"""