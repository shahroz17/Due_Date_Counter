import unittest
import main


class TestTask(unittest.TestCase):

    def test_range(self):
        result = main.total <= 5
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
