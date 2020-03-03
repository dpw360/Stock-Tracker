### IMPORTS ###
import json

### FUNCTIONS ###
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
    elif com[0:6] == "switch":
        switchPortfolio(com[7:])
        return
    elif com == "new portfolio":
        newPortfolio()
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
    print("\nHere is a list of all available commands in Stock Tracker:")
    print("\t- Type a ticker symbol to see that stock's information.")
    print("\t  The default view includes the stock's ticker, price,")
    print("\t  percent changed, open, close, high, and low info, and its")
    print("\t  weekly performance table, as well as how much you own if you")
    print("\t  own any in your portfolio.\n")

    print("\t- Type 'portfolio' to see your portfolio's information.")
    print("\t  Shows you all the stocks you have added to your portfolio,")
    print("\t  with the same default info as looking at any ticker.\n")

    print("\t- Type 'new portfolio' to start a new portfolio. You will be")
    print("\t  prompted to enter a name for the portfolio. The program")
    print("\t  will then switch the current portfolio to the new one.\n")

    print("\t- Type 'switch <portfolio name>' to a different portfolio.")
    print("\t  If the portfolio specified does not exist, you will stay")
    print("\t  on the current portfolio.\n")

    print("\t- Type 'add <ticker symbol>' to add shares to your portfolio.")
    print("\t  Starts the dialog for adding a stock to the current portfolio.")
    print("\t  It will ask you to enter the ticker, and how many shares you")
    print("\t  own.\n")

    print("\t- Type 'worth' to see how much money your portfolio is worth.")
    print("\t  Calculates and displays how much your entire current portfolio")
    print("\t  is worth at the current time. Requires an internet connection.\n")

    print("\t- Type 'settings' to adjust settings for the program.")
    print("\t- Type 'quit' to exit this program.")

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