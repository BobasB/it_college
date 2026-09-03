import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)