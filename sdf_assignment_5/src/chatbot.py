"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

from chatbot import  ACCOUNTS

def get_account() -> int:
    try:
        account_number = int(input("Please enter your account number: "))
        if account_number not in ACCOUNTS:
            raise ValueError("Account number entered does not exist.")
    except ValueError:
        raise ValueError("Account number must be a whole number.")

    return account_number

def get_balance(account: int) -> str:

# Check if the account number exists in the ACCOUNTS dictionary
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    
    # Retrieve the balance from the ACCOUNTS dictionary based on the account parameter
    balance = ACCOUNTS[account]

  # Check if the balance value is in the correct format (string or real number)
    if not isinstance(balance, (str, int, float)):
        raise ValueError("Invalid balance format.")

    # Convert the balance value to a float if it's not already
    if not isinstance(balance, float):
        try:
            balance = float(balance)
        except ValueError:
            raise ValueError("Invalid balance format.")

    # Return a string message with the account number and its balance
    return f"Your current balance for account {account} is ${balance:.2f}."
    
    

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:




## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:


                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""