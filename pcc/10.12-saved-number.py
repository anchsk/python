from pathlib import Path
import json

path = Path('pcc/fave.json')
number = ''
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
else:
    number = input("What's your favorite number?\n")    
    contents = json.dumps(number)
    path.write_text(contents)

print(f"I know your favorite number: {number}")