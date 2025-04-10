import requests 
import json
import pandas as pd

url = 'https://official-joke-api.appspot.com/jokes/ten'
data = requests.get(url)
results = json.loads(data.text)

print(results[0])

""" def get_jokes():
    jokes = []
    for result in results:
        print('!', result)
        jokes.append({ 'setup': result['setup'],
                      'punchline': result['punchline'] })
    
    return jokes

df = pd.DataFrame(get_jokes())
print(df) """
    
    
# Solution:
df = pd.DataFrame(results)
df.drop(columns=["type","id"], inplace=True)
print(df)