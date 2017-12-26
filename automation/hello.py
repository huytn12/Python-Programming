# This program says hello and asks for my name


print('Hello, What is your name? ')
myName = input()


print("It's nice to meet you " + myName)
print('The length of your name is ' + str(len(myName)))

print("How old are you? ")
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in 1 year')
