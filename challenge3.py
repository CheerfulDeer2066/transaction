"""
Caiden Lineman
6/1/2022
This program will keep track of user data in a bank account,
saving various bits of information about
past transactions that can be used for future ones
"""
import datetime
# file of previous transaction values
# global because opened by multiple functions
filePath = 'C:/Users/Caden/Documents/Python/Python Projects/transaction/pastTransactions.txt'

def beginTransaction():
    # create a list for the current transaction data
    # add name to transaction
    transactionInfo = [input("Full Name: ").title()]

    # add date to transaction
    date = datetime.date.today()
    transactionInfo.append(date)

    # find users' most recent transaction (if applicable)
    lastTransaction = findUserAccount(transactionInfo)

    if lastTransaction == -999:  # if the user wants to end the program
        return  # preferably would restart program instead but recursion broke literally everything to just dies instead
    elif lastTransaction == -1:
        currentBalance = 0
        transactionInfo.append(currentBalance)
    else:
        currentBalance = findCurrentBalance(lastTransaction)
        transactionInfo.append(currentBalance)

    print(f"Current Balance: ${transactionInfo[2]}")


"""
Possible Return Values for findUserAccount:
    -1: Create a new account for the user
    -999: End the program
    else: User's most recent transaction was at this index in the file (should work for any file length)
"""
def findUserAccount(transactionInfo):
    # open file of previous transaction values
    file = open(filePath)

    # create list of names of past users (names on any line indexes that are divisible by 7)
    pastUsers = []
    for i, line in enumerate(file):
        if i == 0 or i % 7 == 0:  # names in past transactions are saved on multiples of 7
            pastUsers.append(line.strip())

    # starting at the end, search through names
    for i in range(len(pastUsers)):
        currentTransactionIndex = len(pastUsers) - (i + 1)
        # check if a name matches name in current transaction's data
        if transactionInfo[0] == pastUsers[currentTransactionIndex]:
            print("User Found!")
            # Return first line index of current user's most recent transaction
            # this number is the line index of the user's name (1 less than the line number)
            file.close()
            return (currentTransactionIndex * 7)
        elif currentTransactionIndex == 0:  # name was not found in any transaction
            print("User not Found...")
            # ask if user wants to create an account or end the program
            prompt = input(f"Would you like to open an account under the name {transactionInfo[0]}?: ")
            while prompt not in ["yes", "y", "no", "n"]:  # ensure input is valid
                print("Invalid Response")
                prompt = input(f"Would you like to open an account under the name {transactionInfo[0]}?: ")
            if prompt in ["yes", "y"]:  # create new account (no line index found, so return -1 for if statement)
                file.close()
                return -1
            else:  # end program via if statement later
                print("---")
                file.close()
                return -999


def findCurrentBalance(accountLineNumber):
    # open file of previous transaction values
    file = open(filePath)

    balanceIndex = accountLineNumber + 5
    for i, line in enumerate(file):
        if i == balanceIndex:
            file.close()
            return float(line[14:-1])

beginTransaction()
