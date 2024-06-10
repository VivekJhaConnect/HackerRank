# Read the number of contacts from input
number_of_contacts = int(input().strip())
phone_book = {}

# Read each contact and add it to the phone book
for _ in range(number_of_contacts):
    contact = input().strip()
    name, number = contact.split()
    phone_book[name] = number

# Continue to read input until EOF for querying
try:
    while True:
        query_name = input().strip()
        if query_name in phone_book:
            print(f"{query_name}={phone_book[query_name]}")
        else:
            print("Not found")
except EOFError:
    pass
