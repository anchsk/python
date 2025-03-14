from datetime import datetime
current_time = datetime.now()
# count to 1000000
list = range(1,1000000+1)
print(min(list), max(list))
print(sum(list)) 
new_time = datetime.now()
delta = new_time - current_time
print(delta)
# 0:00:00.025756 to sum 1 million numbers
