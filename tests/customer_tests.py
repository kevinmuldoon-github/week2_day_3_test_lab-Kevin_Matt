import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John", 50)

    def test_customer_have_name(self):
        self.assertEqual("John", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)


    
