import random

exitChoice = "Nothing"
while exitChoice != "EXIT":

    """Import random is used
    for challenges in the
    game with random numbers
    being generated.
    """
    player = ["A Teacher", "A Golfer", "A Coder", "An Egg"]
    reason = ["Money", "Respect", "Revenge", "Fun"]
    outfit = ["Naked", "All Black", "Regular Clothes", "Egg Outfit"]      

    print(f"{random.choice(player)} is robbing the bank for {random.choice(reason)} wearing {random.choice(outfit)}")
    input("Press enter to continue\n")
    print("You’re attempting to pull off a heist.")
    print("You’ll need to navigate the bank, facing multiple challenges.")
    print("Reach the vault without alerting the guards, you’ll win.")

    print("You have four ways to break in")
    print("1, Back Alley")
    print("2, Roof")
    print("3, Underground")
    print("4, Pose as an Employee")

    # Allows the user to input their answer into the terminal
    playerChooses = input("Choose 1, 2, 3 or 4\n")

    if playerChooses == "1":
        print("\nYou decide to take the back alley route as per your planning.")
        print("There is a weak wall which leads to the underground tunnel")
        print("To get to the vault you need to reach the underground")
        print("Using the floor plans you acquired you know the route")
        print("After following your route you reach a door, will you:/n")
        print("1. Enter the door")
        print("2. Wait and see if anyone exits")

        alleyChoice = input("Choose 1 or 2\n")

        if alleyChoice == "1":
            print("You enter the door without checking for guards")
            print("You’re lucky, no one is there.")
            print("You continue your journey to the vault and reach a keypad")
            print("This wasn’t in the planning.")
            print("You need the correct code to pass this door.")
            print("This number is between 1 - 5")

            # Converts the input into an int
            keypadChoice = int(input("Enter the combination\n"))
            # Random number between 1 - 5 is generated
            if keypadChoice == random.randint(1, 5):
                print("The keypad lights up green.")
                print("You were correct, the vault door is unlocked.")
            else:
                print("The keypad lights up red.")
                print("The guards are alerted.")
                print("Game over!")

        elif alleyChoice == "2":
            print("You wait to see if anyone exits the door.")
            print("You've been reported as entering the bank")
            print("The guards check and find your access hole.")
            print("You’re grabbed from behind by the guards - caught waiting!")
            print("Game Over!")

        else:
            print("You need to make a decision, 1 or 2.")

    # End of path 1

    elif playerChooses == "2":
        print("You decide to use the roof access to enter the bank")
        print("After reaching the roof, you open the vent and enter the bank.")
        print("To get to the vault you need to reach the underground")
        print("Using the floor plans you acquired you know the route.")
        print("After following your route you reach a decision, will you:")
        print("1. Continue down the stairs")
        print("2. Use the lift shaft")

        roofChoice = input("Choose 1 or 2\n")

        if roofChoice == "1":
            print("You decide to continue down the staircase.")
            print("Distant talking can be heard")
            print("Two guards are waiting at the bottom, you run.")
            print("Guards are coming down the stairs at the same time.")
            print("You’re caught by the guards and taken away.")
            print("Game Over!")

        elif roofChoice == "2":
            print("Using the rope you packed, you make a knot,")
            print("you descend down the shaft.")
            print("On the wall you see three numbers")
            print("6, 9 and 2")
            print("You reach the bottom floor and check for guards")
            print("After checking for guards, you exit the lift shaft.")
            print("You head towards the vault and approach a keypad")
            print("You'll need to input the correct 3 digit code to enter")

            keypadInput = None
            while True:
                # User will have to keep answering until they get the answer
                keypadInput = input("Enter combination:\n")
                if keypadInput.isdigit() and (
                    int(keypadInput) > 268 and int(keypadInput) < 270
                ):
                    keypadInput = int(keypadInput)
                    break
                else:
                    print("Input was not valid, try again. \n")
                    continue

    # End of path 2

    elif playerChooses == "3":
        print("You decide to use an access tunnel directly into the vault")
        print("Using the underground access, you reach the wall")
        print("Do you use a silent drill or sledgehammer?")
        groundChoice = input("Choose drill or hammer\n")

        if groundChoice == "drill":
            print("Using the silent drill you begin drilling")
            print("Slowly you create a hole wide enough to fit through")
            print("You enter the hole facing the vault")

        elif groundChoice == "hammer":
            print("Obviously you choose to hammer the wall")
            print("The noise starts to gain you unwanted attention..")
            print("Guards are alerted.")
            print("Game Over...... obviously.")
        else:
            print("You need to make a decision, drill or hammer.")

    # End of path 3

    elif playerChooses == "4":
        print("You suit up in your bank uniform")
        print("ID Number 2914")
        print("Name, Danial B Cooper")
        print("Date of birth 24/11/1971")
        print("Walking confidently into the bank towards the security")
        print("You're asked a question by the security")
        print("What is the date of birth on your ID card?")
        employeeChoice = input("Enter your answer:\n")

        if employeeChoice == "24/11/1971":
            print("The guard nods and you go through.")
        else:
            print("The guard grabs you")
            print("You got the answer wrong")
            print("Game Over!")

    # End of path 4

    # Easter egg
    if playerChooses == "easteregg":
        print("Image of egg will appear here")
        print("Congratulations.")

    exitChoice = input("Press return to play again or type EXIT!\n")
