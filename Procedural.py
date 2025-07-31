import random

randomNumber = random.randrange(1, 20)
guessNumber = int(input("Guess a number between 1 and 20: "))

while guessNumber != randomNumber:
    if guessNumber > randomNumber:
        print("Your guess is high")
    elif guessNumber < randomNumber:
        print("Your guess is low")

    guessNumber = int(input("Guess a number between 1 and 20: "))

print("Your guess is correct. Well done!")
