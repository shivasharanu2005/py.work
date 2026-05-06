import random

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess == number:
        print("Correct! You win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")