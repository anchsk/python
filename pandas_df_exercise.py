import pandas as pd

data = {'Product': ['A', 'B', 'A', 'C', 'B'],
        'Price': [10, 20, 12, 15, 18]}

df = pd.DataFrame(data)
"""
print(df)
print(df.iloc[0:2]) # first two rows
print(list(df.columns)) # names of all the columns
print(df.shape) # (5,2)
print(type(df.shape)) # <class 'tuple'>
"""
# Select only the product column
print(list(df['Product'])) 
# Select rows where price is greater than 15
print(df[df['Price'] > 15])
print(type(df[df['Price'] > 15])) # <class 'pandas.core.frame.DataFrame'>
print(df.loc[0,'Price'])
print(df.iloc[1,1])

df['Quantity'] = [5,10,7,8,6]
print(df)

df['Price'] = df['Price'] * 1.1 
print(df['Price'].sum()/df['Price'].size) # mean price
print(df['Price'].mean()) # mean price
print(df['Price'].max()) # highest price

print(df['Product'].unique())
print(df['Product'].value_counts()) # the number of times unique product appears

data_2 = {'Product': ['B', 'D', 'A'],
         'Discount': [0.1, 0.2, 0.05]}

# merge 2 dataframes
df_2 = pd.DataFrame(data_2)
merged_df = pd.merge(df, df_2, on='Product', how='left')
print(merged_df)