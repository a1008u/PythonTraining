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
        count_sortを利用したソート。
        count_sortに規則を与えたイメージ

        対象データ: 24,10,11,324,201,101,55

        - 1回目→: 10,11,201,101,24,324,55 -> 1桁目
        - 2回目←: 201,101,10,11,24,324,55 -> 2桁目（10の位）
        - 3回目→: _10,_11,_55,101,201,324 -> 3桁目（100の位）
        '''

        max_num: int = max(nums)
        place: int = 1
        while max_num > place:
            nums = count_sort(nums, place)
            place *= 10
        return nums
