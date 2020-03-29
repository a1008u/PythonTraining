# coding: utf-8
from typing import List

from src.StopWatch import stop_watch

@stop_watch
class Solution:
    def insertion_sort(self, nums: List[int]) -> List[int]:

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
