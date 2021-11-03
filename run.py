print("You’re attempting to pull off a heist.")
print("You’ll need to navigate the bank, facing multiple challenges.")
print("If you can reach the vault without alerting the guards, you’ll win.")

print("You have four ways to break in")
print("1, Back Alley")
print("2, Roof")
print("3, Underground")
print("4, Pose as an Employee")

playerChooses = input("Choose 1, 2, 3 or 4")

if playerChooses == "1":
    print("You decide to take the back alley route as per your planning.")
    print("There is a weak wall which leads directly to the underground tunnel")
    print("To get to the vault you need to reach the underground")
    print("Using the floor plans you acquired you know the route")
    print("After following your route you reach a door, will you:")
    print("1. Enter the door ")
    print("2. Wait and see if anyone exits")

    alleyChoice = input("Choose 1 or 2")

    if alleyChoice == "1":
        print("You enter the door without checking for guards")
        print("You’re lucky, no one is there.")
        print("You continue your journey to the vault and reach a keypad")
        print("This wasn’t in the planning.")
        print("You need the correct code to pass this door.")

    elif alleyChoice == "2":
        print("You wait to see if anyone exits the door.")
        print("You've been reported as a suspicious person entering the bank.")
        print("The guards check and find your access hole.")
        print("You’re grabbed from behind by the guards - caught waiting!")
        print("Game Over!")

    else:
        print("You need to make a decision, 1 or 2.")

