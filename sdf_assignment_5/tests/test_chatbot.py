"""""
Description: Testing of the chatbot functions.
Author: Manjot Kaur
Date: 2023-10-29
Usage: To test the function in chatbot program.
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection
from src.chatbot import VALID_TASKS, ACCOUNTS

class ChatbotTests(unittest.TestCase):
    def test_get_account_is_valid(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]
        
        # Act
            actual = get_account()

        # Assert
        expected = 123456
        self.assertEqual(expected, actual)
    
    def test_get_account_is_non_numeric(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

        # Act
            with self.assertRaises (ValueError) as context:
                get_account()
            
        # Assert
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_not_exist(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]

        # Act
            with self.assertRaises(Exception) as context:
                get_account()

        # Assert
            self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_get_amount_is_valid(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["500.01"]

        # Act
            actual = get_amount()

        # Assert
        expected = 500.01
        self.assertEqual(expected,actual)

    def test_get_amount_is_non_numeric(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

        # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

        # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    def test_get_amount_is_not_positive(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["0"]

        # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

        # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")

    def test_get_balance_is_correct(self):
        # Arrange
        account_number = 123456

        # Act
        actual = get_balance(account_number)

        # Assert
        expected = "Your current balance for 123456 is $1000.00."
        self.assertEqual(expected,actual)

    def test_get_balance_account_does_not_exist(self):
        # Arrange
        account_number = 112233

        # Act
        with self.assertRaises(Exception) as context:
            get_balance(account_number)

        # Assert
        self.assertEqual(str(context.exception),"Account number does not exist.")

    def test_make_deposit_balance_is_updated(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        amount = 1500.01

        # Act
        make_deposit(account_number, amount)

        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)
    
    def test_make_deposit_correct_value_is_returned(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        amount = 1500.01
        
        # Act
        actual = make_deposit(account_number, amount)
         
        # Assert
        expected = "You have made a deposit of 1500.01 to account 123456."
        self.assertEqual(expected,actual)

    def test_make_deposit_account_does_not_exist(self):
        # Arrange
        account_number = 112233
        amount = 1500.01

        # Act
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, amount)

        # Assert
        self.assertEqual(str(context.exception),"Account number does not exist.")

    def test_make_deposit_amount_is_less_than_zero(self):
        # Arrange
        account_number = 123456
        amount = -50.01

        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)

        # Assert
        self.assertEqual(str(context.exception),"Invalid Amount. Amount must be positive.")

    def test_user_selection_valid_lowercase_selection_by_user(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["balance"]

        # Act
            actual = user_selection()

        # Assert
            expected = "balance"
            self.assertEqual(expected, actual)

    def test_user_selection_valid_wrong_case_selection_by_user(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["DEPOSIT"]

        # Act
            actual = user_selection()

        # Assert
        expected = "deposit"
        self.assertEqual(expected, actual)

    def test_user_selection_invalid_selection_by_user(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["invalid selection"]

        # Act
            with self.assertRaises(ValueError) as context:
                user_selection()

        # Assert
            self.assertEqual(str(context.exception),"Invalid task. Please choose balance, deposit, or exit.")

