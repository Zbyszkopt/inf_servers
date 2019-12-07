# Karol Talaga 302929, Zbigniew Żeglecki 302947
import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    def test_exception_throw(self):
        products = [Product('PP235', 2), Product('PP234', 1), Product('PP233', 3), Product('PP232', 7)]
        for server_type in server_types:
            server = server_type(products)
            self.assertRaises(TooManyProductsFoundError, server.get_entries, 2)


class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_total_price_for_exeptional_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 1), Product('PP237', 5),
                    Product('PPP238', 1)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))

    def test_total_price_for_sum_eq_0_execution1(self):

        products = [Product('PP234', 0), Product('PP235', 0), Product('PP236', 0), Product('PP237', 0),
                    Product('PPP238', 1)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))

    def test_total_price_for_sum_eq_0_execution2(self):
        products = [Product('PP234', 0), Product('PP235', 0), Product('PP236', 0), Product('PP237', 0),
                    Product('PPP238', 1)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(4))

if __name__ == '__main__':
    unittest.main()