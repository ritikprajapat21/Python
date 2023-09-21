import random

number = random.randint(1, 20)

for i in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess > number:
        print('Your guess is too high')
    elif guess < number:
        print('Your guess is too low')
    else:
        break

if guess == number:
    print(f"Goodjob! you took {i} guesses")
else:
    print(f"The number I was thinking was {number}")
