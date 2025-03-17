from pathlib import Path

path = Path(__file__).parent / "learning_python.txt" 
total_count = 0
with open(path) as file:
    content = path.read_text().rstrip()
    for line in content.splitlines():
        total_count += line.count("Python")
print(f"Python mentioned {total_count} times")

