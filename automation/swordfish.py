# This program ask for a name and password.
# Using continue and break statement in while loop


while True:
    print('Who are you')
    name = input()
    if name != 'Joe':
        print('Your name is not listed in the database. Please re-enter your name: ')
        continue
    print('Hello Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')