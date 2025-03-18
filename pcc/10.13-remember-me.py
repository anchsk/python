from pathlib import Path
import json

def get_name():
    while True: # an infinite loop will execute until the return is triggered
        name = input("What's your name? ")
        if name:
            return name
        else:
            print("Please enter a valid name.")


def get_food():
    while True:
        food = input("What's your favorite food? ")
        if food:
            return food
        else:
            print("Please, enter some food!")

def get_number():
    while True:
        number = input("What's your favorite number? ")
        try: # convert to number
            number = int(number)
            return number
        except:
            print("Please, enter a valid number!")
    
path = Path(__file__).parent / "user-info.json"

user_info = dict()

try:
    name = get_name()
    food = get_food()
    number = get_number()
    user_info["name"] = name
    user_info["food"] = food
    user_info["number"] = number
    # raise ValueError('A very specific bad thing happened.')

    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"Data saved to {path}")
except Exception as e:
    print(str(e))
    

