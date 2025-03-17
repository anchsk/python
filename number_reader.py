from pathlib import Path
import json

path = Path('numbers.json')
if path.exists():
    contents = path.read_text()
    numbers = json.loads(contents)
    print(numbers)
else:
    print("Path doesn't exist")

# [2,3,5,7,11,13]


