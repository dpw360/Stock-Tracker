### IMPORTS ###
import json

# Displays a welcome message, only at the start of the program
def welcome():
    print("Welcome to Stock Tracker!")
    print("If you know what you're doing, go ahead and enter a command!")
    print("Otherwise, type 'help' to see your options.")
    print("Common Options:")
    print("\t- Type a ticker symbol to see that stock's information.")
    print("\t- Type 'portfolio' to see your portfolio's information.")
    print("\t- Type 'add <ticker symbol>' to add shares to your portfolio.")
    print("\t- Type 'worth' to see how much money your portfolio is worth.")
    print("\t- Type 'quit' to exit this program.")

# Constantly running while not already in a command. Passes control to the
# necessary function as specified by the user.
def parseCommand(com):
    if com == "help":
        help()
        return
    elif com == "portfolio":
        portfolio()
        return
    elif com[0:3] == "add":
        add(com[4:])
        return
    elif com == "worth":
        worth()
        return
    elif com[0:4] == "comp":
        compare(com[5:])
        return
    elif com == "quit":
        quit()
    else:
        stockInfo(com)
        return 

# Displays information meant to assist with using this application. Will
# display all commands and explain what they are used for.
def help():
    return

# Displays information about the user's portfolio. Includes what stocks are
# owned, quantity owned, prices of all owned stocks, and other info that is
# configurable by the user.
def portfolio():
    return

# Input: A string of form "AAAA"
# Adds a quantity of a stock to a user's portfolio.
def add(stock):
    return

# Calculates the total worth of the user's portfolio.
def worth():
    return

# Input: A string of form "AAAA BBBB"
# Compares the information of two stocks. The info provided is configurable
# by the user.
def compare(stocksString):
    return

# Input: A string of the form "AAAA"
# Gives the info for the stock requested by the user. The info provied is
# configurable by the user.
def stockInfo(stock):
    return

### MAIN ###
welcome()
with open('settings.json') as settings:
    settingsDict = json.load(settings)

while True:
    command = input()
    parseCommand(command)