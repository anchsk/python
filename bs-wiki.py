import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

tables = pd.read_html(URL)
df = tables[2] # the required table will have index 2

print(df.head)

# Example: 
# hyperlinks also get printed (see [n 1])
# 2               China   19535000  ...           17963170  [n 1]2022
