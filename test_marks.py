
import unittest
from unittest.mock import patch
from io import StringIO
from student_marks import calculate_result


class TestStudentMarks(unittest.TestCase):

    @patch("builtins.input", side_effect=["Janaki", "85", "90", "80"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_pass_result(self, mock_stdout, mock_input):
        calculate_result()
        output = mock_stdout.getvalue()
        self.assertIn("Percentage: 85.00%", output)
        self.assertIn("Result: PASS", output)

    @patch("builtins.input", side_effect=["Rahul", "20", "90", "80"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_fail_result(self, mock_stdout, mock_input):
        calculate_result()
        output = mock_stdout.getvalue()
        self.assertIn("Result: FAIL", output)

    @patch("builtins.input", side_effect=["Asha", "120", "80", "70"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_marks(self, mock_stdout, mock_input):
        calculate_result()
        output = mock_stdout.getvalue()
        self.assertIn("Marks must be between 0 and 100", output)

    @patch("builtins.input", side_effect=["Asha", "abc", "80", "70"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        calculate_result()
        output = mock_stdout.getvalue()
        self.assertIn("Please enter valid numeric marks", output)


if __name__ == "__main__":
    unittest.main()