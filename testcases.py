import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
#Although it will pass the test because doubling 2 happens to be the same as 2 squared, I would still consider this code incorrect because the intention is to double, not square, and it would still not work for other numbers.