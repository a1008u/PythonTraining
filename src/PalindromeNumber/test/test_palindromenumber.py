# coding: utf-8
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

import unittest
from src.PalindromeNumber.palindromenumber import Solution

class MyTestCase(unittest.TestCase):
    def test_ispalindrome_ok_1(self):
        """ 成功のテスト
        """
        input: int = 121
        solution: Solution = Solution()
        actual: int = solution.isPalindrome(input)
        self.assertEqual(actual, True)

    def test_ispalindrome_ok_2(self):
        """ 成功のテスト
        """
        input: int = 1221
        solution: Solution = Solution()
        actual: int = solution.isPalindrome(input)
        self.assertEqual(actual, True)

    def test_ispalindrome_ok_3(self):
        """ 成功のテスト
        """
        input: int = 12621
        solution: Solution = Solution()
        actual: int = solution.isPalindrome(input)
        self.assertEqual(actual, True)

    def test_ispalindrome_ng_1(self):
        """ 失敗のテスト
        """
        input: int = -121
        solution: Solution = Solution()
        actual: int = solution.isPalindrome(input)
        self.assertEqual(actual, False)

    def test_ispalindrome_ng_2(self):
        """ 失敗のテスト
        """
        input: int = 12100
        solution: Solution = Solution()
        actual: int = solution.isPalindrome(input)
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()
