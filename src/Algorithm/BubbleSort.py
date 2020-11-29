# coding: utf-8
from typing import List

# from Algorithm.StopWatch import stop_watch
from src.Algorithm.StopWatch import stop_watch


@stop_watch
class Solution:
    """
    bubble sortのイメージ
    対象データ: 2,1,5,8,7,3

    - 1回目: 2,1,5,7,3 | 8
    - 2回目: 2,1,5,3 | 7,8
    - 3回目: 2,1,3 | 5,7,8
    - 4回目: 2,1 | 3,5,7,8
    - 5回目: 1 | 2,3,5,7,8
    """

    def bubble_sort(self, nums: List[int]) -> List[int]:

        for index, _ in enumerate(nums):
            print(index)
            for j in range(len(nums) - index - 1):
                if nums[j] > nums[j + 1]:
                    print(j, j + 1, nums[j], nums[j + 1])
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
                    print(j, j + 1, nums[j], nums[j + 1])
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    change = True

        return nums
