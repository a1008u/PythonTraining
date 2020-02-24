# coding: utf-8
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            horizontal scanningの理解
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        preStr: str = strs.pop(0)
        for index, targetStr in enumerate(strs):
            while strs[index].find(preStr):
                preStr = preStr[0:len(preStr) - 1]
                if len(preStr) == 0:
                    return ""
        return preStr
