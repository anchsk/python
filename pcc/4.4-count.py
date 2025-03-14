from datetime import datetime
current_time = datetime.now()
# count to 1000000
for i in range(1,1000):
    print(i)
new_time = datetime.now()
delta = new_time - current_time
print(delta)
# 0:00:03.288767 to count until 1 million
# 0:00:00.000290 form 100 items
