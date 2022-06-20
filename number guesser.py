number = randint(1, 9)
tries = 5

print ("Guess the number, beware: you only have 5 tries! (Hint: it's between 1 and 9)")

guess = int(input("Type in your guess: "))

if guess < number:
    print ("Incorrect! Try higher.")
    print (guess)
    tries -= 1
if guess > number:
    print ("Incorrect! Try lower.")
    print (guess)
    tries -= 1
if guess == number:
    print ("Congratulations! You got it!")
#I searched it up and it said you use randint for a random number but it doesn't work
