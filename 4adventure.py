name = input("Type in your name: ")
print("Welcome ", name, "to the adventure quest!")
print("\nYou woke up in a jungle 2 days ago. You reach a crossroad, do you want to walk straight up or swim across the river?")

answer = input("\nEnter 'walk' or 'swim' to continue: ").lower()
if answer == "walk" :
    answer = input("\nYou hit a fork, do you want to go left or right? Enter 'left' or 'right' to continue: ").lower()
    if answer == "left" :
        answer = print("\nYou come across a tiger. Guess what, he is hungry and eats you. You dead.")
    elif answer == "right" :
        print("Always choose right, you exit the jungle. You WIN.")
    else :
        print("Coward, you lose.")
elif answer == "swim" :
    print("You dead, crocodile eat you.")
else :
    print("Coward, you lose.")

print("\nThank you for playing. See you again.\n")