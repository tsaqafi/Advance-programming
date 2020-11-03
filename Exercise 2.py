# Ask the user for a number. Depending on
# whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an
# even / odd number react
# differently when divided by 2?

num = int(input("Choose a number: "))
num_choose = num % 2

if num_choose == 1:
    print("The number is odd")
else:
    print("The number is even")