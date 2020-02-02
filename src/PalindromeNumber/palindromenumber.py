import math


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber: int = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = math.floor(x / 10)

        return x == revertedNumber or x == math.floor(revertedNumber/10)
