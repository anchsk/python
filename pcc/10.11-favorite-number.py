from pathlib import Path
import json

fav_number = input("What's your favorite number?\n")
path = Path('pcc/fave.json')
contents = json.dumps(fav_number)
path.write_text(contents)
