import unittest
from main import count_string

class TestFunction(unittest.TestCase):
    def test_my_function(self):
        self.assertIsInstance(count_string("no"), int)
        self.assertEqual(count_string("Два"), 3)

if __name__ == '__main__':
    unittest.main()
