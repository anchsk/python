import pandas as pd # panda means panel data (data sets)

""" pre-build classes and functions """
csv_path = 'file1.csv' # csv path
df = pd.read_csv(csv_path) # df - data frame
df.head() # examine the first row

print(df.head(0))

# songs = { 'key': ['val', 'val']}
# pd.DataFrame(songs)

# row index, col index
# df.iloc([1,2]) 

# create a Series from a list
data = [10,20,30,40,50]
s = pd.Series(data)
print(s[2], s.iloc[3])
# 30 40
print(s[1:3])
""" 
1    20
2    30
dtype: int64
"""
print(s[1:3].values)
# [20 30]
print(s)
""" 
0    10
1    20
2    30
3    40
4    50
dtype: int64
"""
print(s.values)
# [10 20 30 40 50]
print(type(s))
# <class 'pandas.core.series.Series'>