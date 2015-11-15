import unittest
from cashdesk import Bill, BillBatch, CashDesk


class CashDeskTest(unittest.TestCase):
    def setUp(self):
        self.test_bill = Bill(20)

    def test_create_new_bill_class(self):
        self.assertTrue(isinstance(self.test_bill, Bill))

    def test_create_int_value_from_bill(self):
        self.assertEqual(int(self.test_bill), 20)

    def test_amount_in_bill(self):

        with self.assertRaises(AttributeError):
            self.test_bill.amount

    def test_str_dunder_for_bill(self):
        self.assertEqual(str(self.test_bill), "A 20$ bill.")

    def test_repr_dunder_for_bill(self):
        self.assertEqual(repr(self.test_bill), "A 20$ bill.")

    def test_eq_between_bills_when_not_same(self):
        bill1 = Bill(20)
        bill2 = Bill(11)

        self.assertTrue(bill1 != bill2)

    def test_eq_between_bills_when_same(self):
        bill1 = Bill(20)
        bill2 = Bill(20)

        self.assertTrue(bill1 == bill2)

    def test_bills_are_orderable(self):
        self.assertTrue(Bill(5) < Bill(20))

    def test_can_hash_bill(self):
        self.assertIsNotNone(hash(self.test_bill))

    def test_can_put_bill_in_dictionary(self):
        money_holder = {}
        bill = Bill(20)
        money_holder[bill] = 1
        self.assertTrue(bill in money_holder)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            Bill(-100)

    def test_value_error_raises_from_zero_amount(self):
        with self.assertRaises(ValueError):
            Bill(0)

    def test_can_create_billbatch(self):
        batch = BillBatch([])
        self.assertTrue(isinstance(batch, BillBatch))

if __name__ == '__main__':
    unittest.main()
