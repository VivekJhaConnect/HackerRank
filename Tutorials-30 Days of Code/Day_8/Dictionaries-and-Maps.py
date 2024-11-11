# Read the number of contacts from input
number_of_contacts = int(input())
phone_book = {}

# Read each contact and add it to the phone book
for _ in range(number_of_contacts):
    contact = input().strip()
    name, number = contact.split()
    phone_book[name] = number

# Query the phone book for each name provided
for _ in range(number_of_contacts):
    query_name = input().strip()
    if query_name in phone_book:
        print(f"{query_name}={phone_book[query_name]}")
    else:
        print("Not found")