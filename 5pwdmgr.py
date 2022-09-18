from function5 import check, view, add

master_password = input("\nEnter master password: ").encode()

if not check(master_password) :
    print("Invalid")
    quit()
else :
    print("\nCongrats you are in..\n")

while True :
    todo = input("\nEnter 'add' or 'view' to add or view passwords, 'q' to quit: ")
    todo = todo.lower()

    if todo == 'add' :
        add()
    elif todo == 'view' :
        view()     
    elif todo == 'q' :
        print("Exited.")
        break
    else :
        print("Invalid. Exited.")
        break