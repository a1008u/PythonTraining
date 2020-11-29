# coding: utf-8
from typing import List
import logging

from src.Algorithm.StopWatch import stop_watch


class Solution:

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    @stop_watch
    def quick_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        left, right, same = [], [], 0

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                same = 1

        logging.info("----------------------------")
        logging.info(
            'left is %s | [pivot] * same is %s | right is %s',
            left,
            [pivot] * same,
            right)
        logging.info("----------------------------")

        left: List[int] = self.quick_sort(left)
        right: List[int] = self.quick_sort(right)

        logging.info("=========================")
        logging.info(
            'left is %s | [pivot] * same is %s | right is %s',
            left,
            [pivot] * same,
            right)
        logging.info('result is %s', left + [pivot] * same + right)
        logging.info("=========================")
        return left + [pivot] * same + right

    @stop_watch
    def quick_sort2(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[0]

        left: List[int] = [i for i in nums[1:] if i <= pivot]
        right: List[int] = [i for i in nums[1:] if i > pivot]

        left: List[int] = self.quick_sort2(left)
        right: List[int] = self.quick_sort2(right)

        logging.info("=========================")
        logging.info(
            'left is %s | [pivot] * same is %s | right is %s',
            left,
            [pivot],
            right)
        logging.info('result is %s', left + [pivot] + right)
        logging.info("=========================")
        return left + [pivot] + right

    @stop_watch
    def partition(self, nums: List[int], low: int, high: int) -> int:
        i: int = low - 1
        pivot: int = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    @stop_watch
    def quick_sort3(self, nums: List[int]) -> List[int]:
        """
         対象データ: 2,1,5,8,7,3  pivot:_, i=-1, j=0

        - 1-1回目: 2,1,5,8,7,3 pivot:3, i=0, j=0
        - 1-1回目: 2,1,5,8,7,3 pivot:3, i=1, j=1
        - 1-1回目: 2,1,5,8,7,3 pivot:3, i=1, j=2
        - 1-1回目: 2,1,5,8,7,3 pivot:3, i=1, j=3
        - 1-1回目: 2,1,5,8,7,3 pivot:3, i=1, j=4
        - 2,1,3,8,7,5
        - 2-1回目: 2,1 | 3,8,7,5 pivot:1, i=0, j=0
        - 1,2 | 3,8,7,5
        - 3-1回目: 1,2,3 | 8,7,5 pivot:5, i=0, j=0
        - 3-2回目: 1,2,3 | 8,7,5 pivot:5, i=0, j=1
        - 3-2回目: 1,2,3 | 8,7,5 pivot:5, i=0, j=2
        - 1,2,3,5 | 7,8
        - 4-1回目: 1,2,3,5 | 7,8 pivot:8, i=0, j=0
        - 4-2回目: 1,2,3,5 | 7,8 pivot:8, i=0, j=1
        - 1,2,3,5,7,8
        """
        @stop_watch
        def _quick_sort(nums: List[int], low: int, high: int) -> None:
            if low < high:
                partition_index: int = self.partition(nums, low, high)
                _quick_sort(nums, low, partition_index - 1)
                _quick_sort(nums, partition_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)
        return nums
