import unittest
from ChangeCalculator import _getChangeRecursive, exactChange
class TestChangeCalculator(unittest.TestCase):
    def test__getChangeRecursive(self):
        assert(_getChangeRecursive(6, [5, 2, 2, 2]) == [2, 2, 2,])
        assert(_getChangeRecursive(1, [2]) == False)
        assert(_getChangeRecursive(11, [10, 5, 2, 1]) == [1, 10])
        assert(_getChangeRecursive(100, [10, 5, 2, 1]) == False)

    def test_exactChange(self):
        assert(exactChange(1.50,[[0.03, 0.9], [0.10, 3], 
                                [0.12, 6], [0.02, 0.5], 
                                [0.50, 3]]) == "SUFFICIENT COINS")

        assert(exactChange(0.50, [[0.15, 0.6]]) == "INSUFFICIENT COINS")

if __name__ == '__main__':
    unittest.main()