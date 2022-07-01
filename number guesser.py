import random

number = random.randint(1, 9)
tries = 5
guess = 0

print ("Guess the number, beware: you only have 5 tries! (Hint: it's between 1 and 9)")

while number != guess:
    guess = int(input("Type in your guess: "))

if guess == number:
    print ("Congratulations! You got it!")
