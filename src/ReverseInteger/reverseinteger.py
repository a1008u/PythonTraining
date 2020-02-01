# coding: utf-8
import math
import sys


class Solution:
    def reverse(self, x: int) -> int:
        rev: int = 0

        chang: bool = False
        if x < 0:
            x *= -1
            chang = True

        while x != 0:
            pop: int = x % 10
            x = math.floor(x / 10)
            if rev > 2147483647/10 or (rev == 2147483647/10 and pop > 7):
                return 0
            if rev < -2147483648/10 or (rev == -2147483648/10 and pop < -8):
                return 0

            rev = rev * 10 + pop

        if chang:
            return -1 * rev

        return rev
