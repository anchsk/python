import unittest

from mymodule import square, doubler

# inherits the unittest.TestCase


class TestMyModule(unittest.TestCase):
    # only functions starts with test_ are run
    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_doubler(self):
        self.assertEqual(doubler(0), 0)


if __name__ == '__main__':
    unittest.main()
""" 
unittest.main() discovers test cases automatically (classes that inherit
unittest.TestCase and runs the test)

if __name__ == '__main__':
ensures that the test runs only when executed directly, 
not when it's imported as a module into another file
"""
