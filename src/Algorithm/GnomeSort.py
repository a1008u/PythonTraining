# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def gnome_sort(self, nums: List[int]) -> List[int]:

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

