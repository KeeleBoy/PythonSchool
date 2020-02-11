# This is a guess the number game.
import random

#Number guessing
#Author Kyle Warchuck
#9/16/17
#this program creates a random number between 1 and 10 and gives you 10 chances to guess the numbers

#initalize number of guesses taken
guessesTaken = 0

#Calculate random number
number = random.randint(1, 10)

#Display the question
print("I am thinking of a number between 1 and 10, you have 10 tries. Can you guess it?")

#loop while guesses are less than 10
while guessesTaken < 10:
    print("What is your guess?: ") 
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

#Displays hints
    if guess < number:
        print("Woah, your guess is too low, try again") 

    if guess > number:
        print("Woah, your guess is too high, try again.")

    if guess == number:
        break

#Display number found
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job! You guessed it in " + guessesTaken + " tries the correct number was " + str(number))

#Display missed number
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)
