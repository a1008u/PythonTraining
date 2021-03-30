# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def shell_sort(self, nums: List[int]) -> List[int]:
        '''
        Shell_Sortの説明
        事前にGAPを決めて、そちらを使って一定の区間でsortをしていく
        ＊Insertion sortの改良

        対象データ: 2,1,5,8,7,3

        - 1回目: 2,1,5,8,7,3 -> 2,1,5,8,7,3 gap=3, temp=8
        - 2回目: 2,1,5,8,7,3 -> 2,1,5,8,7,3 gap=3, temp=7
        - 3回目: 2,1,5,8,7,3 -> 2,1,3,8,7,5 gap=3, temp=3
        - 4回目: 2,1,5,8,7,3 -> 1,2,3,8,7,5 gap=1, temp=1
        - 5回目: 2,1,5,8,7,3 -> 1,2,3,8,7,5 gap=1, temp=3
        - 6回目: 2,1,5,8,7,3 -> 1,2,3,7,8,5 gap=1, temp=8
        - 7回目: 2,1,5,8,7,3 -> 1,2,3,7,5,8 -> 1,2,3,5,7,8 gap=1, temp=5
        '''

        len_nums: int = len(nums)
        gap: int = len_nums // 2
        while gap > 0:
            for i in range(gap, len_nums):
                temp = nums[i]
                j: int = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap //= 2
        return nums
