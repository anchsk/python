import pandas as pd
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 10, 'b': 20, 'c': 30, 'd': 40},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000},
           ]
df = pd.DataFrame(mydict)
# print(df)
""" 
      a     b     c     d
0     1     2     3     4
1    10    20    30    40
2   100   200   300   400
3  1000  2000  3000  4000 
"""

print(df.iloc[0,0]) # 1
print(df.iloc[0,2]) # 3
print(df.iloc[1:3,2]) # 30, 300


[7,5] # wrong
[6,4]

# from row 3 through row 6
# df.loc[2:5, 'Album'] 
# 3,4,5,6
# 2:6
