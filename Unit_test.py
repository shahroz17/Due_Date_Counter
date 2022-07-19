import unittest
import DueDate


class TestTask(unittest.TestCase):

    def test_range(self):
        result = DueDate.total <= 5
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()