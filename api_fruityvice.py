import requests
import json
import pandas as pd

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)

df = pd.DataFrame(results)

df2 = pd.json_normalize(results) # nested json becomes flat
print(df2.iloc[0])
""" 
name                        Persimmon
id                                 52
family                      Ebenaceae
order                         Rosales
genus                       Diospyros
nutritions.calories                81
nutritions.fat                    0.0
nutritions.sugar                 18.0
nutritions.carbohydrates         18.0
nutritions.protein                0.0 
"""

cherry = df2.loc[df2["name"]=="Cherry"]
banana = df2.loc[df2["name"]=="Banana"]

print(cherry.iloc[0]['family'], cherry.iloc[0][8])
print('Banana', banana.iloc[0]['nutritions.calories'])