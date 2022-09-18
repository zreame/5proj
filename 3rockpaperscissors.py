import random

user_wins = 0
computer_wins = 0
choices = ["paper", "scissors", "rock"]

while True :
    user_input = input("Type rock, paper or scissors, or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices :
        continue

    random_num = random.randint(0, 2)
    com_choice = choices[random_num]

    print (f"me choose: {com_choice}")

    if choices.index(user_input) == random_num :
        print("Draw.")
        print(f"Computer: {computer_wins}, User: {user_wins}")
    elif choices.index(user_input) == 2 and random_num == 0 :
        computer_wins += 1
        print("You lose.")
        print(f"Computer: {computer_wins}, User: {user_wins}")
    elif random_num == 2 and choices.index(user_input) == 0 :
        user_wins += 1
        print("You win.")
        print(f"Computer: {computer_wins}, User: {user_wins}")
    elif choices.index(user_input) == random_num - 1 :
        computer_wins += 1
        print("You lose.")
        print(f"Computer: {computer_wins}, User: {user_wins}")
    else :
        user_wins += 1 
        print("You win.")
        print(f"Computer: {computer_wins}, User: {user_wins}")

print("goodbye!")