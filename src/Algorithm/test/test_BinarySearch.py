from src.Algorithm.BinarySearch import Solution
import unittest
import sys
import os
from typing import List

print('prepare test start-----------------------')
path = os.path.join(os.path.dirname(__file__), '../../../')
sys.path.append(path)
sys.path.append('/root/src/')
print(sys.path)
print(dir())
print('prepare test end-----------------------')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 28
        solution: Solution = Solution()
        result: int = solution.linear_seach(nums, targetInt)

        self.assertEqual(nums.index(targetInt), result)

    def test_something_2(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 3333
        solution: Solution = Solution()
        result: int = solution.linear_seach(nums, targetInt)

        self.assertEqual(-1, result)

    def test_something_3(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 3333
        solution: Solution = Solution()
        result: int = solution.binary_search(nums, targetInt)

        self.assertEqual(-1, result)

    def test_something43(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 28
        solution: Solution = Solution()
        result: int = solution.binary_search(nums, targetInt)

        self.assertEqual(nums.index(targetInt), result)

    def test_something_5(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 3333
        solution: Solution = Solution()
        result: int = solution.binary_search2(nums, targetInt)

        self.assertEqual(-1, result)

    def test_something_6(self):
        nums: List[int] = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
        targetInt: int = 28
        solution: Solution = Solution()
        result: int = solution.binary_search2(nums, targetInt)

        self.assertEqual(nums.index(targetInt), result)


if __name__ == '__main__':
    unittest.main()
