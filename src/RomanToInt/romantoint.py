import string


class Solution:
    def romanToInt(self, s: str) -> int:
        num: int = 0
        preNum: int = 5000
        for r in s:
            xx: int = self.transfer(r)
            if preNum < xx:
                num = num - preNum + xx - preNum
            else:
                num += xx
                preNum = xx
        return num

    @staticmethod
    def transfer(s: string) -> int:
        bricks: list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        bricksVal: list = [1, 5, 10, 50, 100, 500, 1000]
        for i, v in enumerate(bricks):
            if v == s:
                return bricksVal[i]
        return 0

    def romanToIntV2(self, s):
        roman: dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        resultNum = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                resultNum = resultNum + roman[s[i]] - 2 * roman[s[i-1]]
            else:
                resultNum += roman[s[i]]
        return resultNum
