# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


@stop_watch
class Solution:
    def select_sort(self, nums: List[int]) -> List[int]:

        for index, _ in enumerate(nums):
            min: int = index
            for ckTargetIndex in range(index + 1, len(nums)):
                if nums[min] > nums[ckTargetIndex]:
                    min = ckTargetIndex
            nums[index], nums[min] = nums[min], nums[index]

        return nums
