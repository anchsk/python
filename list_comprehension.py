list = ['a', 'b', 'c', 'd']
updated_list = [str(a) * 2 for a in list if a != 'a']
print(updated_list)
# ['bb', 'cc', 'dd']
