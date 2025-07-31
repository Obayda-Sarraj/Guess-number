import random

class GuessGame:
    def __init__(self):
        self.number = random.randrange(1, 20)
        self.guess = 0

    def play(self):
        while self.guess != self.number:
            self.guess = int(input("Guess number 1 to 20: "))
            if self.guess > self.number:
                print("Your guess is high")
            elif self.guess < self.number:
                print("Your guess is low")
        print("correct")

game = GuessGame()
game.play()
