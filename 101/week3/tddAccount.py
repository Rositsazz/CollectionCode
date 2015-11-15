import unittest
from BankAccount import BankAccount


class BankAcoountTest(unittest.TestCase):

    def test_exists_class(self):
        account = BankAccount("Rado", 100, "$")
        self.assertTrue(isinstance(account, BankAccount))

    def test_name_is_str(self):
        with self.assertRaises(TypeError):
            BankAccount(10, 100, "$")

    def test_balance_is_int(self):
        with self.assertRaises(TypeError):
            BankAccount("Rado", "a", "$")

    def test_currency_is_str(self):
        with self.assertRaises(TypeError):
            BankAccount("Rado", 100, 15)

    def test_balance_is_not_int(self):
        with self.assertRaises(TypeError):
            BankAccount("Rado", "100", "$")

    def test_value_error_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Rado", -10, "$")

    def test_account_has_amount(self):
        account = BankAccount("Rado", 100, "$")
        old_balance = account.get_balance()
        amount = 100
        account.deposit(amount)
        new_balance = account.get_balance()
        self.assertTrue(old_balance == new_balance - amount)

    def test_amount_is_int(self):
        account = BankAccount("Rado", 100, "$")
        with self.assertRaises(TypeError):
            account.deposit("test")

    def test_evaluate_withdraw(self):
        account = BankAccount("Rado", 100, "$")
        old_balance = account.get_balance()
        amount = 100
        account.withdraw(amount)
        new_balance = account.get_balance()
        self.assertEquals(old_balance, new_balance + amount)

    def test_withdraw_bigger_than_balance(self):
        account = BankAccount("Rado", 100, "$")
        old_balance = account.get_balance()
        amount = 200
        account.withdraw(amount)
        new_balance = account.get_balance()
        print(new_balance)
        with self.assertRaises(ValueError):
            self.assertTrue(old_balance == new_balance)


if __name__ == '__main__':
    unittest.main()
