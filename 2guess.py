import random

def checkdigit(user) :
    try :
        return int(user)
    except :
        print("\nnot an integer, exiting..\n")
        quit()

upper_bound = input("\nEnter max number: \n")
# randint includes upper bound, here 10, randrange does not include upper bound
correct = random.randint(1, checkdigit(upper_bound))
tries = 0

while True :
    tries += 1
    guess = input(f"Guess an number between 1 and {upper_bound}: \n" )
    guess = checkdigit(guess)

    if guess < 1 or guess > checkdigit(upper_bound) :
        print ("Integer out of bounds, exiting..\n")
        break

    if guess == correct :
        print(f"\nYou are correcto! Total tries: {tries}.\n")
        break
    elif guess < correct :
        print("\ntry higher\n")
        continue
    elif guess > correct :
        print("\ntry lower\n")
        continue
