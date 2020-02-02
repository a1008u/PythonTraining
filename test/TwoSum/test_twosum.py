# coding: utf-8
# import sys
# sys.path.append('/home/circleci/workspace/src/TwoSum')
# print(sys.version)
# print(sys.prefix)
# print(sys.path)

import unittest
from typing import List

from src.TwoSum.twosum import Solution


class MyTestCase(unittest.TestCase):
    def test_twosumSuccess1(self):
        """ 成功のテスト
        """
        nums: List[int] = [2, 3, 7, 321]
        target: int = 9
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSum(nums, target)

        self.assertEqual(0, twosumResult[0])
        self.assertEqual(2, twosumResult[1])

    def test_twosumSuccess2(self):
        """ 成功のテスト
        """
        nums: List[int] = [3, 2, 4]
        target: int = 6
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSum(nums, target)

        self.assertEqual(1, twosumResult[0])
        self.assertEqual(2, twosumResult[1])

    def test_twosumDict1(self):
        """ 成功のテスト
        """
        nums: List[int] = [3, 2, 4, 5]
        target: int = 6
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSumDict(nums, target)

        self.assertEqual(1, twosumResult[0])
        self.assertEqual(2, twosumResult[1])

    def test_twosumDict2(self):
        """ 成功のテスト
        """
        nums: List[int] = [2, 7, 11, 15]
        target: int = 9
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSumDict(nums, target)

        self.assertEqual(0, twosumResult[0])
        self.assertEqual(1, twosumResult[1])

    def test_twosumDict3(self):
        """ 成功のテスト
        """
        nums: List[int] = [3, 3]
        target: int = 6
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSumDict(nums, target)

        self.assertEqual(0, twosumResult[0])
        self.assertEqual(1, twosumResult[1])

    def test_twosumDictOnePass(self):
        """ 成功のテスト
        """
        nums: List[int] = [3, 3]
        target: int = 6
        solution: Solution = Solution()
        twosumResult: List[int] = solution.twoSumDictOnePass(nums, target)

        self.assertEqual(0, twosumResult[0])
        self.assertEqual(1, twosumResult[1])

if __name__ == '__main__':
    unittest.main()
