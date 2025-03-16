""" write a program that:
- reads the file 
- prints it twice (as a whole file, and by line)
"""

from pathlib import Path

path = Path(__file__).parent / "learning_python.txt" 
with open(path, 'r') as file:
    content = path.read_text().rstrip()
    print(content)
    for line in file: 
        print('line:', line)

lines = content.splitlines() # list of lines
for line in lines:
    message = line
    message = message.replace('Python', 'C')
    print(line, message)


for line in content.splitlines():
    print("Printing a line again! {}".format(line))
    
