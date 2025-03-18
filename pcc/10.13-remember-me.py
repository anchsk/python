from pathlib import Path
import json

path = Path(__file__).parent / "user-info.json"


def check_name(new_name):
    if not path.exists():
        print("File does not exist!")
        exit()
    contents = path.read_text()
    user_info = json.loads(contents)
    saved_name = user_info["name"]
    print('saved_name', user_info["name"])
    if saved_name == new_name:
        return True
    else:
        print("not the same!")
        return False
    
    
def get_name():
    while True: # an infinite loop will execute until the return is triggered
        name = input("What's your name? ")
        if check_name(name):
            # check_name(name)
            print('Check executed')
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
    

