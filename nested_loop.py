import time
start_time = time.time()

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

count = 0
# outer loop
for x in list1:
    count += 1
    # inner loop
    for y in list2:
        count += 1

print(count)
# 90

# outer loop (first iteration)
for i in range(4): #row
    # inner loop (all iterations)
    for j in range(10): #column
        print(0,end = " ")
    print()
    
print(round((time.time() - start_time), 2))