
"""
Description: Chatbot application. It provides user to
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Jasleen kaur
Date: 22 March,2024
Usage: From the console: python src/chatbot.py
"""



## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:
    """
    Returns an integer if it is valid, after getting the input from user.

    Returns:
        int: Valid account number entered by the user.

    Raises:
        ValueError: If the user enters a non-integer value.
        Exception: If any unexpected error occurs.
    
    """
    try:
        account_number = int(input("Please enter your account number: "))
    except ValueError:
        raise ValueError("Account number must be a whole number.")
    
    if account_number not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    
    return account_number

def get_amount() -> float:
    """
    Returns a float value, after getting the input from user.

    Returns:
        float: The amount is deposited.

    Raises:
        ValueError: If the user enters a non-numeric or a non-positive number.
    
    """

    try:
        transaction_amount = float(input("Enter the transaction amount: "))
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
    
    if transaction_amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    
    return transaction_amount

def get_balance(account_number: int) -> str:
    """
    Returns the balance of a specific account.

    Args:
        account_number(int): The account number.
    
    Returns:
        str: A message having the account balance and account number.

    Raises:
        Exception: If the account number does not exist in ACCOUNTS.
    
    """

    if account_number not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    
    balance = ACCOUNTS[account_number]["balance"]

    return f"Your current balance for {account_number} is ${balance:.2f}."

def make_deposit(account_number: int, amount: float) -> str:
    """
    Returns the account balance after adding the amount to it.

    Args:
        account_number(int): The account number.
        amount(float): The amount that is to deposit in account.

    Returns:
        str: A message having the updated balance and account number.

    Raises:
        Exception: If the account number does not exist.
        ValueError: If the amount is not greater than zero.
    
    """

    if account_number not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    
    ACCOUNTS[account_number]["balance"] += amount
    return f"You have made a deposit of {amount:.2f} to account {account_number}."

def user_selection() -> str:
    """
    Returns the valid task entered by user.

    Returns:
        str: The task selected by user.

    Raises:
        ValueError: If an invalid user selection is provided.

    """
    user_input = input("What would you like to do (balance/deposit/exit)? ").lower()
    if user_input in VALID_TASKS:
        return user_input
    else:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    
## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

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
            ## CALLING THE user_selection FUNCTION 
            selection = user_selection()

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALLING THE get_account FUNCTION
                        account = get_account()

                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALLING THE get_balance FUNCTION
                        balance = get_balance(account)
                        print(balance)

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALLING THE get_amount FUNCTION 
                            amount = get_amount()

                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    
                    ## CALLING THE make_deposit FUNCTION 
                    make_deposit(account, amount) 
                    print(f"You have made a deposit of ${amount:.2f} to account {account}.")

            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
   
if __name__ == "__main__":
     chatbot()