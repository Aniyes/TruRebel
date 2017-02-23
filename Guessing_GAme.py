# This is a Guess the Number game.
import random

Guesses = 0

print('Hello! What is your name?')

Name = input()
Number = random.randint(1, 10)
print( Name + ', I am thinking of a number between 1 and 10. You have 7 tries!')

while Guesses < 6:
    print('What am I thinking?') 
    Guess = input()
    Guess = int(Guess)
    Guesses +=  1

    if Guess < Number:
        print('too low.')

    if Guess > Number:
        print('too high.')

    if Guess == Number:
        break

if Guess == Number:
    Guesses = str(Guesses)
    print(Name + '! You Guessed my Number in ' + Guesses + ' Guesses!')

if Guess != Number:
    Number = str(Number)
    print('The number was ' + Number)