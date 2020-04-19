import random

guesses = 0

number = random.randint(1, 500)
# print(number) //Allows you to see the random number for testing purposes.

name = input("Hi, this is my number guessing game, please enter your name.\n")
print("\nHello " + name + ", you have 10 guesses to guess a number between 1 and 500\n")

while guesses < 10:
    guess = int(input("Enter a number between 1 and 500.\n"))

    #    if guess < 1:
    #       input("Please enter a number between 1 and 20\n")
    #   elif guess > 20:
    #       input("Please enter a number between 1 and 20\n")

    guesses = guesses + 1

    if guess < number:
        print("\nYour guess is too low.\n")
    elif guess > number:
        print("\nYour guess is too high.\n")
    else:
        break

if guess == number:
    guesses = str(guesses)
    print("\nCongratulations " + name + ", you used " + guesses + " guesses\n")

if guess != number:
    number = str(number)
    print("\nSorry " + name + ", you did not guess correctly, the number was " + number)
