# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def gnome_sort(self, nums: List[int]) -> List[int]:

        '''
        gnome_sortの説明


        GnomeSortの改良

        対象データ: 2,1,5,8,7,3

        - 1回目: 2,1,5,8,7,3 -> 1,2,5,8,7,3
        - 2回目: 1,2,5,8,7,3 -> 1,2,5,8,3,7 -> 1,2,5,3,8,7 -> 1,2,3,5,8,7
        - 3回目: 1,2,3,5,8,7 -> 1,2,3,5,7,8
        '''

        len_nums: int = len(nums)
        index: int = 0

        while index < len_nums:
            if index == 0:
                index += 1

            if nums[index] >= nums[index-1]:
                index += 1
            else:
                nums[index], nums[index-1] = nums[index-1], nums[index]
                index -= 1

        return nums

