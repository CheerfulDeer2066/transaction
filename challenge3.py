"""
Caiden Lineman
6/1/2022
This program will keep track of user data in a bank account,
saving various bits of information about
past transactions that can be used for future ones
"""
import datetime

def beginTransaction():
    # open file of previous transaction values
    file = "C:\\Users\Robotics\Desktop\Caiden\exam\pastTransactions.txt"
    file = open(file)

    # create a list for the current transaction data
    transactionInfo = []

    # add name to transaction
    transactionInfo.append(input("Full Name: ").title())

    # add date to transaction
    date = datetime.date.today()
    transactionInfo.append(date)

    # find users' most recent transaction (if applicable)
    lastTransaction = findUserAccount(transactionInfo, file)
    if lastTransaction == -999:  # if the user wants to end the program
        return  # preferably would restart program instead but recursion broke literally everything
    elif lastTransaction == -1:
        currentBalance = 0
        transactionInfo.append(currentBalance)
    else:
        findCurrentBalance()


"""
Possible Return Values for findUserAccount:
    -1: Create a new account for the user
    -999: End the program
    else: User's most recent transaction was at this index in the file
"""
def findUserAccount(transactionInfo, file):
    # create list of names of past users (names on any line indexes that are divisible by 7)
    pastUsers = []
    for i, line in enumerate(file):
        if i == 0 or i % 7 == 0:  # if on line 2, print current line
            pastUsers.append(line.strip())

    # starting at the end, search through names
    for i in range(len(pastUsers)):
        currentTransactionIndex = len(pastUsers) - (i + 1)
        # check if a name matches name in current transaction's data
        if transactionInfo[0] == pastUsers[currentTransactionIndex]:
            print("User Found!")
            recentTransactionLine = (currentTransactionIndex * 7) + 1
            break
        elif currentTransactionIndex == 0:  # name was not found in any transaction
            print("User not Found...")
            # ask if user wants to create an account or end the program
            prompt = input(f"Would you like to open an account under the name {transactionInfo[0]}?: ")
            while prompt not in ["yes", "y", "no", "n"]: # ensure input is valid
                print("Invalid Response")
                prompt = input(f"Would you like to open an account under the name {transactionInfo[0]}?: ")
            if prompt in ["yes", "y"]:  # create new account (no line index found, so return -1)
                return -1
            else:  # end program
                print("---")
                return -999

    # Return first line index of current users' most recent transaction
    # this number is 1 the line index of the users' name (1 less than the line number)
    return (currentTransactionIndex * 7)

def findCurrentBalance():
    pass
    """
    check at the most recent transaction index + 5
    start the search at an index that ignores "New Balance: $",
    as this part is constant and is present in every transaction
    return this value as the user's current balance for use in the new transaction
    """

beginTransaction()
