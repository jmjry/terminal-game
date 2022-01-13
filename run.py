import random
import os

"""Import random is used
    for challenges in the
    game with random numbers
    being generated.
    """


def clear_terminal():
    """
    Clears the terminal window prior to new content.
    Original code from
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    Recommended to me by Matt Bodden
    https://github.com/MattBCoding
    """
    os.system("cls" if os.name == "nt" else "clear")


def check_input(prompt, valid_inputs, error_message):
    """
    User inputs the prompt, valid inputs and error message.
    This can be changed each time the function is called
    """
    input_valid = False
    while input_valid is False:
        user_input = input(prompt)
        if user_input not in valid_inputs:
            print(error_message)
        else:
            input_valid = True
    return user_input


def main():
    # The main function contains the game structure
    exit_choice = ""
    while exit_choice != "EXIT":
        """exitChoice will allow
        the user to exit the game at
        anytime by typing EXIT
        """
        player = [
            "a Teacher",
            "a Golfer",
            "a Coder",
            "an Egg",
            "a Civilian",
            "a Bank Guard",
            "Aquaman",
        ]
        reason = ["Money", "Respect", "Revenge", "Fun"]
        outfit = [
            "Crocs, just crocs",
            "a Balaclava",
            "Regular Clothes",
            "an Egg Outfit",
            "your Uniform",
        ]

        print(
            f"You're {random.choice(player)}\n"
            "You're robbing the bank because you want "
            f"{random.choice(reason)}\n"
            f"You're doing this wearing {random.choice(outfit)}\n"
        )
        # Randomly generates a character for the user
        check_input(
            "Press enter to continue\n", [""], "Incorrect input, press enter."
        )

        print("You’re attempting to pull off a heist.")
        print("You’ll need to navigate the bank, facing multiple challenges.")
        print("Reach the vault without alerting the guards, you’ll win.")

        print("You have four ways to break in")
        print("1, Back Alley")
        print("2, Roof")
        print("3, Underground")
        print("4, Pose as an Employee")

        player_chooses = check_input(
            "Choose 1, 2, 3 or 4.\n",
            ["1", "2", "3", "4"],
            "You must choose 1, 2, 3 or 4",
        )

        # Allows the user to choose their route in the game

        if player_chooses == "1":
            print("\nYou decide to take the back alley route as per planning.")
            print("There is a weak wall which leads to the underground tunnel")
            print("To get to the vault you need to reach the underground")
            print("Using the floor plans you acquired you know the route")
            print("After following your route you reach a door, will you:/n")
            print("1. Enter the door")
            print("2. Wait and see if anyone exits")

            alley_choice = check_input(
                "Choose 1 or 2\n", ["1", "2"], "You must choose 1 or 2"
            )

            if alley_choice == "1":
                print("You enter the door without checking for guards")
                print("You’re lucky, no one is there.")
                print("You continue to the vault and reach a keypad")
                print("This wasn’t in the planning.")
                print("You need the correct code to pass this door.")
                print("This number is between 1 - 5")

                keypad_choice = check_input(
                    "Enter the combination\n",
                    ["1", "2", "3", "4", "5"],
                    "You must pick between 1 to 5",
                )
                if keypad_choice == random.randint(1, 5):
                    # Random number between 1 - 5 is generated
                    print("The keypad lights up green.")
                    print("You were correct, the vault door is unlocked.")
                else:
                    print("The keypad lights up red.")
                    print("The guards are alerted.")
                    print("Game over!")

            elif alley_choice == "2":
                print("You wait to see if anyone exits the door.")
                print("You've been reported as entering the bank")
                print("The guards check and find your access hole.")
                print("You’re grabbed by the guards - caught waiting!")
                print("Game Over!")

            else:
                print("You need to make a decision, 1 or 2.")

        # End of path 1

        elif player_chooses == "2":
            print("You decide to use the roof access to enter the bank")
            print("After reaching the roof, you open and enter the vent.")
            print("To get to the vault you need to reach the underground")
            print("Using the floor plans you acquired you know the route.")
            print("After following your route you reach a decision, will you:")
            print("1. Continue down the stairs")
            print("2. Use the lift shaft")

            roof_choice = check_input(
                "Choose 1 or 2\n", ["1", "2"], "Invalid input, pick 1 or 2"
            )

            if roof_choice == "1":
                print("You decide to continue down the staircase.")
                print("Distant talking can be heard")
                print("Two guards are waiting at the bottom, you run.")
                print("Guards are coming down the stairs at the same time.")
                print("You’re caught by the guards and taken away.")
                print("Game Over!")

            elif roof_choice == "2":
                print("Using the rope you packed, you make a knot,")
                print("you descend down the shaft.")
                print("On the wall you see three numbers")
                print("6, 9 and 2")
                print("You reach the bottom floor and check for guards")
                print("After checking for guards, you exit the lift shaft.")
                print("You head towards the vault and approach a keypad")
                print("You'll need to input the correct 3 digit code to enter")

                keypad_input = None
                while True:
                    keypad_input = input("Enter combination:\n")
                    if keypad_input.isdigit() and (
                        int(keypad_input) > 268 and int(keypad_input) < 270
                    ):
                        keypad_input = int(keypad_input)
                        print("The keypad lights green.")
                        print("You were correct, the vault door is unlocked.")
                        print("Congratulations, you won!")
                        break
                    else:
                        print("Input was not valid, try again. \n")
                        continue

        # End of path 2

        elif player_chooses == "3":
            print("You decide to use an access tunnel directly into the vault")
            print("Using the underground access, you reach the wall")
            print("Do you use a silent drill or sledgehammer?")
            ground_choice = check_input(
                "Choose drill or hammer\n",
                ["drill", "hammer"],
                "Pick either drill or hammer",
            )

            if ground_choice == "drill":
                print("Using the silent drill you begin drilling")
                print("Slowly you create a hole wide enough to fit through")
                print("You enter the hole facing the vault")
                print("To enter the vault you'll need to crack the keypad")
                keypad_crack = check_input(
                    "\nChoose to hack or smash the keypad\n",
                    ["hack", "smash"],
                    "You need to pick either smash or hack.",
                )

                if keypad_crack == "hack":
                    print("You decide to hack the keypad")
                    print("You'll need to solve multiple puzzles")
                    check_input(
                        "Press enter on the keypad to start.\n",
                        [""],
                        "Wrong input, press enter to begin.",
                    )
                    print("If 1=3")
                    print("2=3")
                    print("3=5")
                    print("4=4")
                    print("5=4")
                    puzzle_one = check_input(
                        "Then 6 = ?\n", ["3"], "You got it wrong, try again."
                    )

                    if puzzle_one == "3":
                        print("The keypad lights green")
                        print("You got the first puzzle right!")
                        print("Next question\n")
                        print("There is a three-digit number")
                        print("The second is four times as big as the third")
                        print("while the first is three less than the second")
                        puzzle_two = check_input(
                            "What is the number?\n",
                            ["141"],
                            "You got it wrong, try again.",
                        )

                        if puzzle_two == "141":
                            print("The keypad lights green")
                            print("The vault begins to unlock")
                            print("You've broke into the bank, well done!")
                        else:
                            print("You got it wrong, the keypad lights red")
                            print("The guards come rushing in, game over.")

                elif keypad_crack == "smash":
                    print("As the brave person you are")
                    print("you decide to smash the keypad")
                    print("smashing.......")
                    print("...........")
                    print("the guards hear the smashing")
                    print("game over, you got caught.... obviously.")

                else:
                    print("You got it wrong, the keypad lights red")
                    print("The guards come rushing in and you're captured!")

            elif ground_choice == "hammer":
                print("Obviously you choose to hammer the wall")
                print("The noise starts to gain you unwanted attention..")
                print("Guards are alerted.")
                print("Game Over...... obviously.")
            else:
                print("You need to make a decision, drill or hammer.")

        # End of path 3

        elif player_chooses == "4":
            print("You suit up in your bank uniform")
            print("ID Number 2914")
            print("Name, Daniel B Cooper")
            print("Date of birth 24/11/1971")
            print("Walking confidently into the bank towards the security")
            print("You're asked a question by the security")
            print("What is the date of birth on your ID card?")
            employee_choice = check_input(
                "Enter your answer:\n", ["24/11/1971"], "Wrong answer."
            )

            if employee_choice == "24/11/1971":
                print("The guard nods and you go through.")
                print("You walk down the stairs towards the vault.")
                print("You'll need todays password to enter the vault.")
                print("You could either steal it, guess it or find it.")
                password_finder = check_input(
                    "How will you get the password?\n",
                    ["steal it", "guess it", "eggman", "find it"],
                    "Invalid input, try again.",
                )

                if password_finder == "steal it":
                    print("You decide to steal it from a guard")
                    print("You enter the locker rooms")
                    print("Now you need to find the right locker")
                    print("Searching..... \n")
                    print("Got it, now it's time to break in")
                    print("You've just realised the time, 12pm. Lunchbreak.")
                    print("Guards enter as you crack the locker.")
                    print("Game Over, you got caught!")
                elif password_finder == "guess it":
                    print("You decide to take a wild guess, genius!")
                    password_answer = check_input(
                        "What is the password?\n",
                        ["eggman"],
                        "Wrong answer, try again.",
                    )
                    if password_answer == "eggman":
                        print("The keypad lights green, you actually got it?")
                        print("You now have access to the vault!")
                        print("Congratulations, you won!")
                    else:
                        print("The keypad lights red and the alarms go off.")
                        print("Maybe guessing wasn't the best idea...")
                        print("Game over, you lost!")
                elif password_finder == "find it":
                    print("You decide to find the password in the bank")
                    print("Going upstairs you locate the bank managers office")
                    print("Sneaking in, you look for the password")
                    print("Searching......\n")
                    print("You found it! Today's password is eggman")
                    print("Are you ready to unlock the vault?")
                    password_answer = check_input(
                        "What is the password?\n",
                        ["eggman"],
                        "Wrong answer, try again.",
                    )
                    if password_answer == "eggman":
                        print("The keypad lights green, the vault door opens.")
                        print("You now have access to the vault!")
                        print("Congratulations, you won!")
                    else:
                        print("The keypad lights red, you got it wrong.")
                        print("The alarms ring and guards come rushing.")
                        print("Game over!")
                else:
                    print("Make a decision, steal it, guess it or find it")
            else:
                print("The guard grabs you")
                print("You got the answer wrong")
                print("Game Over!")

        # End of path 4

        # Easter egg
        if player_chooses == "easteregg":
            print("Easter Egg")
            print("Congratulations.")

        exit_choice = check_input(
            "Press enter to continue or EXIT to end \n", [""],
            "Incorrect input, press enter."
        )
    clear_terminal()


if __name__ == "__main__":
    main()
