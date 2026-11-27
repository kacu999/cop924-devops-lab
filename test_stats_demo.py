# test_stats_demo.py
import unittest
from stats_demo import average

class TestAverage(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average([2, 4, 6]), 4.0)

if __name__ == '__main__':
    unittest.main()