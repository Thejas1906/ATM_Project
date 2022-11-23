from tools import *
import pandas as pd
from time import sleep

# Load data from "data.csv" to "df" dataframe
df = pd.read_csv("data.csv", index_col="name")
# print(df)

def UserPanel(name):
    # User Panel Menu
    Menu(f"{name}'s USER PANEL", ["Balance","Withdraw", "Deposit", "Exit"])

    print()
    entry = IntInput("Entry: ", bounds=(1, 4))

    match(entry):
        case 1:
            ClearScreen()
            # Get the balance from dataframe
            balance = df.loc[name, "balance"]
            print(f"{BRIGHT_WHITE}BALANCE{RESET} : {BRIGHT_CYAN}{balance}{RESET}")
            print()
            sleep(1)
            # Recall the method
            UserPanel(name)
        case 2:
            ClearScreen()

            # get the current balance
            balance = df.loc[name, "balance"]

            # Take input in Cyan colour
            print(f"{BRIGHT_WHITE}Current Balance: {BRIGHT_CYAN}{balance}{RESET}")
            print()
            amount = IntInput(f"Withdraw Amount: {CYAN}")
            # Reset the color
            print(RESET, end="")

            print()
            if(amount >= balance):
                print(f"{RED}Insufficient Funds{RESET}")
            elif(amount > (balance - 2000)):
                print(f"{RED}You need minimum 2000 to keep your account running{RESET}")
            else:
                print(f"{GREEN}{amount} has been removed from your account{RESET}")
                df.loc[name, "balance"] -= amount
                balance = df.loc[name, "balance"]
                print(f"{BRIGHT_WHITE}New Balance : {BRIGHT_CYAN}{balance}{RESET}")

            print("redirecting you to the USER PANEL in 3 sec...")
            sleep(3)
            ClearScreen()
            UserPanel(name)
        case 3:
            ClearScreen()

            # get the current balance
            balance = df.loc[name, "balance"]

            print(f"{BRIGHT_WHITE}Current Balance : {BRIGHT_CYAN}{balance}{RESET}")
            print()
            amount = IntInput(f"Deposit Amount: {CYAN}")
            print(f"{RESET}", end="")

            df.loc[name, "balance"] += amount
            balance = df.loc[name, "balance"]
            print()
            print(f"{GREEN}{amount} has been succefully deposited into your account{RESET}")
            print(f"{BRIGHT_WHITE}New Balance: {BRIGHT_CYAN}{balance}{RESET}")
            print("redirecting you to the USER PANEL in 3 sec...")
            sleep(3)
            ClearScreen()
            UserPanel(name)
        case 4:
            pass

def MainMenu():
    # Main Menu Menu
    Menu("MAIN MENU", ["Login to an existing account", "Register a new account","Exit"])

    print()
    # Take numeric entry between 1 to 3
    entry = IntInput("Entry: ", bounds=(1, 3))


    ClearScreen()
    match(entry):
        case 1:
            print(f"{BRIGHT_WHITE}To Authenticate yourselves, please fill in the following details:{RESET}")
            print()

            name = input("Registered Name: ")
            pin = 0
            # Check if the name is in the index of dataframe (Check data.csv for more info)
            if(name not in df.index):
                print()
                print(f"{RED}We do not have this account in our database, consider registering yourselves through the main menu{RESET}")
                print("redirecting you to the main menu in 5 sec...")
                sleep(5)
                ClearScreen()
                MainMenu()
            else:
                pin = IntInput(f"Enter your PIN (4 digit): {CYAN}", digit=4)
                print(RESET, end="")
                if(pin == df.loc[name, "pin"]):
                    print()
                    print(f"{GREEN}You have succefully been authenticated{RESET}")
                    print("redirecting you to the USER PANEL in 3 sec...")
                    sleep(3)
                    ClearScreen()
                    UserPanel(name)
                else:
                    print(f"{RED}Incorrect PIN{RESET}")

        case 2:
            print(f"{BRIGHT_WHITE}To Register yourselves, please fill in the following details:{RESET}")
            print("(2000 registration fees has been paid)")
            print()

            name = input("Your Full Name: ")
            pin = IntInput(f"Enter a PIN (4 digit): {CYAN}", digit=4)
            print(RESET, end="")            
            print()

            # Check if name entered is in the database already
            if(name in df.index):
                print("This Account already Exists")
            else:
                # Add a new row
                df.loc[name] = [pin, 2000]
                print(f"{GREEN}Your Account has been Succesfully Registered{RESET}")
                print("redirecting you to the USER PANEL in 5 sec...")
                sleep(5)
                ClearScreen()
                UserPanel(name)
        case 3:
            pass

    # Save changes made to data to "data.csv"
    df.to_csv("data.csv")

ClearScreen()
MainMenu()
