import unittest
from marks import calculate_result


class TestMarks(unittest.TestCase):

    def test_pass(self):
        total, percentage, result = calculate_result([80, 90, 70])
        self.assertEqual(total, 240)
        self.assertEqual(percentage, 80)
        self.assertEqual(result, "PASS")

    def test_fail(self):
        _, _, result = calculate_result([20, 90, 70])
        self.assertEqual(result, "FAIL")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_result([120, 80, 70])

    def test_empty_marks(self):
        with self.assertRaises(ValueError):
            calculate_result([])


if __name__ == "__main__":
    unittest.main()