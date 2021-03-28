# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def insertion_sort(self, nums: List[int]) -> List[int]:
        '''
        Insertion_sortの説明
        最大実行数は対象データの個数=1の回数分データのソートを行う。
        その際にtempを利用して、値を保持する。

        対象データ: 2,1,5,8,7,3

        - 1回目: 2 | 1,5,8,7,3 -> 1 | 2,5,8,7,3 temp = 1
        - 2回目: 1,2 | 5,8,7,3 -> 1,2 | 5,8,7,3 temp = 5
        - 3回目: 1,2,5 | 8,7,3 -> 1,2,5 | 8,7,3 temp = 8
        - 4回目: 1,2,5,8 | 7,3 -> 1,2,5,7 | 8,3 temp = 7
        - 5回目: 1,2,5,7,8 | 3 -> 1,2,3,5,7 | 8 temp = 3
        '''

        for index in range(1, len(nums)):
            # 現在要素を一時的に記憶する。
            temp: int = nums[index]

            # 直前の位置を記録する。
            targetIndex = index - 1

            while (targetIndex >= 0) and (nums[targetIndex] > temp):
                nums[targetIndex + 1] = nums[targetIndex]
                targetIndex -= 1
            nums[targetIndex + 1] = temp

        return nums
