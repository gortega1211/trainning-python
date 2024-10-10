# target = __import__("my_sum.py")
# sum = target.sum

import unittest

from my_sum import sum_items

class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
            Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum_items(data)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
    # run with 'python -m unittest -v test'
    # run with 'python -m unittest discover'
    # run with 'python -m unittest discover -s test'
    # run with 'python -m unittest discover -s test -t src'