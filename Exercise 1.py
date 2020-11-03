# Create a program that asks the user to enter
# their name and their age. Print out a message
# addressed to them that tells them the year that
# they will turn 100 years old.

name_str = input("What is your name: ")
age = int(input("What is your age: "))
year_hundred = ((2020 - age) + 100)

print(name_str, "will turn 100 year old at", year_hundred)