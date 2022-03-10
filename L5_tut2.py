import random

def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

number = random.randint(1,100)

guess = 0

while guess != number:
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct!")

print("The number was", number)