# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def select_sort(self, nums: List[int]) -> List[int]:

        '''
        Select_Sortの説明
        手前から対象の値を全ての値と比較して、小さい値を昇順に設定する。
        ＊BubbleSortの改良

        対象データ: 2,1,5,8,7,3

        - 1回目: 2,1,5,8,7,3 -> 1,2,5,8,7,3
        - 2回目: 1,2,5,8,7,3 -> 1,2,5,8,7,3
        - 3回目: 1,2,5,8,7,3 -> 1,2,3,8,7,5
        - 4回目: 1,2,3,8,7,5 -> 1,2,3,5,7,8
        - 5回目: 1,2,3,5,7,8 -> 1,2,3,5,7,8
        '''

        for index, _ in enumerate(nums):
            minIndex: int = index
            for ckTargetIndex in range(index + 1, len(nums)):
                if nums[minIndex] > nums[ckTargetIndex]:
                    minIndex = ckTargetIndex
            nums[index], nums[minIndex] = nums[minIndex], nums[index]

        return nums
