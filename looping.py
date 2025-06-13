str = 'looping'

for item in str:
    print(item)
    
for idx, item in enumerate(str):
    print(idx,item)
    
for i in range(10):
    print('looping', i)
    
count = 0
while count < len(str):
    print(str[count])
    count += 1

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Pudding':
#         print('Yes one of my favorite desserts is', dessert) 
#     else:
#         print('No sorry, that dessert is not on my list')
   
   
   
# for-else
for dessert in favorites:
    if dessert == 'Apple Pie':
        print('Yes one of my favorite desserts is', dessert)
        break # without break it will print else
else: # This else belongs to the for loop
    print('No sorry, that dessert is not on my list')


