import unittest

from shipping import shipping_fee_cents


class ShippingTests(unittest.TestCase):
    def test_below_threshold(self):
        for subtotal in (0, 9999):
            with self.subTest(subtotal=subtotal):
                self.assertEqual(shipping_fee_cents(subtotal), 599)

    def test_free_shipping_boundary_and_above(self):
        for subtotal in (10000, 10001):
            with self.subTest(subtotal=subtotal):
                self.assertEqual(shipping_fee_cents(subtotal), 0)

    def test_rejects_negative_subtotal(self):
        with self.assertRaises(ValueError):
            shipping_fee_cents(-1)

    def test_rejects_non_integer_values_and_booleans(self):
        for subtotal in ("10000", 10000.0, None, True):
            with self.subTest(subtotal=subtotal):
                with self.assertRaises(TypeError):
                    shipping_fee_cents(subtotal)


if __name__ == "__main__":
    unittest.main()
