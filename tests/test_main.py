import unittest
from src import main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.main(), None)


if __name__ == "__main__":
    unittest.main()
