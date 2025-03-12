list_of_people = [("mail@example.com", "Anna"), ("mail2@example.com", "Joe")]

# Loop through tuple
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails(list_of_people))



# Enumerate tuple
def full_emails(people):
    result = []
    for i, (email, name) in enumerate(people):
        result.append("{} - {} <{}>".format(i, name, email))
    return result

print(full_emails(list_of_people))
