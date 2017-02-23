# This is a Guess the Number game.
import random

Guesses = 0

print('Hello! What is your name?')

Name = input()

print( Name + ', Think of a number between 1 - 100 . Give me 7 tries!')

Number = int(input())

while Guesses < 6:

    Guess = random.randint(1, 100)
    Guesses += 1

    if Guess < Number:
        print('too low.')

    if Guess > Number:
        print('too high.')

    if Guess == Number:
        break

if Guess == Number:
    Guesses = str(Guesses)
    print(Name + '! I guessed your number in ' + Guesses + ' Guesses!')

if Guess != Number:
    Number = str(Number)
    print('The number was ' + Number)