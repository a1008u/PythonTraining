# coding: utf-8
from typing import List

# from Algorithm.StopWatch import stop_watch
from src.Algorithm import InsertionSort
from src.Algorithm.StopWatch import stop_watch


# def insertion_sort(nums: List[int]):
#     for index in range(1, len(nums)):
#         # 現在要素を一時的に記憶する。
#         temp: int = nums[index]
#
#         # 直前の位置を記録する。
#         targetIndex = index - 1
#
#         while (targetIndex >= 0) and (nums[targetIndex] > temp):
#             nums[targetIndex + 1] = nums[targetIndex]
#             targetIndex -= 1
#         nums[targetIndex + 1] = temp
#     return nums


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

    @stop_watch
    def bucket_sort(self, nums: List[int]) -> List[int]:

        max_num: int = max(nums)
        len_nums: int = len(nums)
        size: int = max_num // len_nums

        buckets: List[List[int]] = [[] for _ in range(max_num + 1)]
        for num in nums:
            i = num // size
            if i != size:
                buckets[i].append(num)
            else:
                buckets[size - 1].append(num)

        solution: InsertionSort.Solution = InsertionSort.Solution()
        for i in range(max_num + 1):
            solution.insertion_sort(buckets[i])

        result: List[int] = []
        for i in range(max_num + 1):
            result += buckets[i]

        return result
