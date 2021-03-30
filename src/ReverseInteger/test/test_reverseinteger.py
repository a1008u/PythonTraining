# coding: utf-8
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

import unittest
from typing import List

from src.ReverseInteger.reverseinteger import Solution


class MyTestCase(unittest.TestCase):
    def test_reverse_ok_1(self):
        """ 成功のテスト
        """
        input: int = 0
        expect: int = 0
        solution: Solution = Solution()
        actual: int = solution.reverse(input)

        self.assertEqual(expect, actual)

    def test_reverse_ok_2(self):
        """ 成功のテスト
        """
        input: int = 123
        expect: int = 321
        solution: Solution = Solution()
        actual: int = solution.reverse(input)

        self.assertEqual(expect, actual)

    def test_reverse_ok_3(self):
        """ 成功のテスト
        """
        input: int = -123
        expect: int = -321
        solution: Solution = Solution()
        actual: int = solution.reverse(input)

        self.assertEqual(expect, actual)

    def test_reverse_ok_4(self):
        """ 成功のテスト
        """
        input: int = 120
        expect: int = 21
        solution: Solution = Solution()
        actual: int = solution.reverse(input)

        self.assertEqual(expect, actual)

    def test_reverse_ok_5(self):
        """ 成功のテスト
        """
        input: int = 1534236469
        expect: int = 0
        solution: Solution = Solution()
        actual: int = solution.reverse(input)

        self.assertEqual(expect, actual)
