import random

highest = 10
answer = random.randint(1, highest)
print(answer) 
guess = ""
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer and guess!=0:
    guess= int(input())

    if guess == answer:
        print("Congratulations! You guessed correctly.")
    else:
        if guess < answer:
            if guess!=0:
                print("Please guess higher")
        else: # guess must be greater than answer, not equal to.
            print ('Please guess lower')
if guess==0:
    print("Coward")
print("Game over.")
