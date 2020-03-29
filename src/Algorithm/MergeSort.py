# coding: utf-8
from typing import List

from src.StopWatch import stop_watch

@stop_watch
class Solution:
    def merge_sort(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left: List[int] = self.merge_sort(nums[:mid])
        right: List[int] = self.merge_sort(nums[mid:])
        print(left, right)

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result: List[int] = []
        i, j = 0, 0

        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i < len(left):
            result.extend(left[i:])

        if j < len(right):
            result.extend(right[j:])

        return result
