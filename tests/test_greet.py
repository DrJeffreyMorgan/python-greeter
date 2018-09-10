import unittest

from greeter import Greeter


class MyTest(unittest.TestCase):

    def test_greet(self):
        greeter = Greeter('World!')
        self.assertEqual(greeter.greet(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
