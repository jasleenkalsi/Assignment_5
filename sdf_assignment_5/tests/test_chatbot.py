"""
Description: 
Author: Jasleen kaur
Date: 03/21/2024
Usage:
"""

import unittest
from unittest.mock import patch

class ChatbotTests(unittest.TestCase): 
  pass
 
from src.chatbot import get_account 
class TestGetAccount(unittest.TestCase):
    def test_valid_account_number(self):
        # Arrange
         with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]
            # Act
            account_number = get_account()
            
            # Assert
            self.assertEqual(account_number, 123456)

    def test_non_numeric_account_number(self):
        # Arrange
         with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

            # Act & Assert
            with self.assertRaises(ValueError) as context:
                get_account()

            self.assertEqual(str(context.exception), "Account number must be a whole number.")

def test_non_existing_account(self):
    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["112233"]

        # Act & Assert
        with self.assertRaises(ValueError):
            get_account()

    if __name__ == "_main_":
      unittest.main()

    
from src.chatbot import get_account, get_balance 
class TestGetBalance(unittest.TestCase):
    def test_valid_account_balance(self):
        # Arrange
        account_number = 123456
        expected_output = 'Your current balance for account 123456 is $1000.00.'

        # Act
        result = get_balance(account_number)

        # Assert
        self.assertEqual(result, expected_output)

class TestGetBalance(unittest.TestCase):
    def test_non_existing_account_balance(self):
        # Arrange
        account_number = 112233

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            get_balance(account_number)

        self.assertEqual(str(context.exception), "Account number does not exist.")

    if __name__ == "_main_":
      unittest.main() 

from src.chatbot import get_account, get_balance 

class TestGetBalance(unittest.TestCase):
    def test_valid_account_balance(self):
        # Arrange
        account_number = 123456
        expected_output = 'Your current balance for account 123456 is $1,000.00.'

        # Act
        balance_message = get_balance(account_number)


        # Assert
        self.assertEqual(balance_message, expected_output)


    def test_non_existing_account_balance(self):
        # Arrange
        account_number = 112233

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            get_balance(account_number)

        self.assertEqual(str(context.exception), "Account number does not exist.")

    if __name__ == "_main_":
      unittest.main()
