# coding: utf-8
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

import string
import unittest

from RomanToInt.romantoint import Solution

class MyTestCase(unittest.TestCase):
    def test_romantoint_ok_1(self):
        input: string = "III"
        expect: int = 3
        solution: Solution = Solution()
        actual: int = solution.romanToInt(input)
        self.assertEqual(actual, expect)
        actual2: int = solution.romanToIntV2(input)
        self.assertEqual(actual2, expect)

    def test_romantoint_ok_2(self):
        input: string = "IV"
        expect: int = 4
        solution: Solution = Solution()
        actual: int = solution.romanToInt(input)
        self.assertEqual(actual, expect)
        actual2: int = solution.romanToIntV2(input)
        self.assertEqual(actual2, expect)


    def test_romantoint_ok_3(self):
        input: string = "LVIII"
        expect: int = 58
        solution: Solution = Solution()
        actual: int = solution.romanToInt(input)
        self.assertEqual(actual, expect)
        actual2: int = solution.romanToIntV2(input)
        self.assertEqual(actual2, expect)

    def test_romantoint_ok_4(self):
        input: string = "MCMXCIV"
        expect: int = 1994
        solution: Solution = Solution()
        actual: int = solution.romanToInt(input)
        self.assertEqual(actual, expect)
        actual2: int = solution.romanToIntV2(input)
        self.assertEqual(actual2, expect)

if __name__ == '__main__':
    unittest.main()
