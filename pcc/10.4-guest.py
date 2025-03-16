

from pathlib import Path

""" guest = input("What's your name?\n")
path = Path(__file__).parent / 'guest.txt'

print(guest)
path.write_text(guest)

 """
# write a guest_book
path = Path(__file__).parent / 'guest_book.txt'
contents = ""
x = 0
while x < 3:
    guest = input("What's your name?\n")
    contents += f"{x+1} {guest}\n"
    x += 1
path.write_text(contents)
