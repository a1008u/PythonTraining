# coding: utf-8
from typing import List

from Algorithm.StopWatch import stop_watch

@stop_watch
class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:

        for index, _ in enumerate(nums):
            print(index)
            for j in range(len(nums) - index - 1):
                if nums[j] > nums[j + 1]:
                    print(j, j+1, nums[j], nums[j + 1])
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

    def bubble_sort2(self, nums: List[int]) -> List[int]:

        change: bool = True
        for index, _ in enumerate(nums):
            if not change:
                break

            print(index)

            change = False
            for j in range(len(nums) - index - 1):
                if nums[j] > nums[j + 1]:
                    print(j, j+1, nums[j], nums[j + 1])
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    change = True

        return nums
