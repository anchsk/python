""" 
Event class:
date
user
machine
type

Problem: we need to process a list of Event objects using their
attributes to generate a report that lists all users currently 
logged in to the machines.

"""

class Event:
    def __init__(self, machine, date, type, user):
        self.date = date
        self.machine = machine
        self.type = type
        self.user = user

events = [Event('machine','2020-01-21 12:45:46', 'login', 'anna'), Event('machine_2', '2020-01-22 15:53:42', 'logout', 'joe'),
          Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'joe'),]

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            # machines[event.machine].discard(event.user) <-- doesn't raise an exception if the item is not in the list
            # or use an if statement
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
            
    return machines

def generate_report(machines):
    for machine,users in machines.items():
        if len(users)>0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))
        

users = current_users(events)
print(users)
generate_report(users)

