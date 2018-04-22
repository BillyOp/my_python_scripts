# This is a guess the number game
import random

print("Hello what's your name")
name = input()

print("Well, " + str(name) + "I am thinking of a number between one and twenty guess the number")
secretNumber = random.randint(1, 20)

print("DEBUG: Secret Number is " + str(secretNumber))

for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too hight")
    else:
        break
    
    # This condition is for the correct guess
if guess == secretNumber:
    print("Good job, " + name + "you guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("The number I was thinking of is " + str(secretNumber))
