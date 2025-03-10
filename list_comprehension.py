list = ['a', 'b', 'c', 'd']
# [expression for item in list if condition]
updated_list = [str(a) * 2 for a in list if a != 'a']
print(updated_list)
# ['bb', 'cc', 'dd']
