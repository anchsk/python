#[(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)....(10,3)]

my_list = []
for x in range(1,11):
    for y in range(1,4):
       # my_list.append(tuple([x,y]))
       my_list.append((x,y))
print(my_list)