# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


def count_sort(nums: List[int], place: int) -> List[int]:
    counts: List[int] = [0] * 10
    result: List[int] = [0] * len(nums)

    for num in nums:
        index: int = int(num / place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    i: int = len(nums) - 1
    while i >= 0:
        index: int = int(nums[i] / place) % 10
        result[counts[index] - 1] = nums[i]
        counts[index] -= 1
        i -= 1

    return result


class Solution:
    @stop_watch
    def radix_sort(self, nums: List[int]) -> List[int]:
        '''
        radix_sortの説明
        count_sortを利用
        swapを利用して変更があったか目印（印）を利用し、
        対象データを-> , <-の流れで入れ替えていく。

        BubbleSortの改良

        対象データ: 2,1,5,8,7,3 swap=false

        - 1回目→: 1,2,5,3,7 | 8 swap=true
        - 2回目←: 1,2,3,5 | 7,8 swap=true
        - 3回目→: 1,2,3 | 5,7,8 swap=false
        '''

        max_num: int = max(nums)
        place: int = 1
        while max_num > place:
            nums = count_sort(nums, place)
            place *= 10
        return nums
