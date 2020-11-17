# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:
    @stop_watch
    def merge_sort(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left: List[int] = self.merge_sort(nums[:mid])
        right: List[int] = self.merge_sort(nums[mid:])
        print(left, right)

        return self.merge(left, right)

    @stop_watch
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

    @stop_watch
    def merge_sort2(self, nums: List[int]) -> List[int]:

        """
        対象データ: 2,1,5,8,7,3

        - leftとrightに分けて、sortする。
        [2,1,5] -> [2] [1] [5] -> [1,2,5]
        [8,7,3] -> [8] [7] [3] -> [3,7,8]

        - 最終的にleftとrightをマージ
        [1,2,3,5,7,8]
        """

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left: List[int] = nums[:mid]
        right: List[int] = nums[mid:]

        self.merge_sort2(left)
        self.merge_sort2(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums
