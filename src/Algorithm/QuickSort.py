# coding: utf-8
from typing import List
import logging

from src.StopWatch import stop_watch

@stop_watch
class Solution:

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

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
        logging.info('left is %s | [pivot] * same is %s | right is %s',  left, [pivot] * same, right)
        logging.info("----------------------------")

        left: List[int] = self.quick_sort(left)
        right: List[int] = self.quick_sort(right)

        logging.info("=========================")
        logging.info('left is %s | [pivot] * same is %s | right is %s', left, [pivot] * same, right)
        logging.info('result is %s',  left + [pivot] * same + right)
        logging.info("=========================")
        return left + [pivot] * same + right


    def quick_sort2(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[0]

        left: List[int] = [i for i in nums[1:] if i <= pivot]
        right: List[int] = [i for i in nums[1:] if i > pivot]

        left: List[int] = self.quick_sort2(left)
        right: List[int] = self.quick_sort2(right)

        logging.info("=========================")
        logging.info('left is %s | [pivot] * same is %s | right is %s', left, [pivot], right)
        logging.info('result is %s',  left + [pivot] + right)
        logging.info("=========================")
        return left + [pivot] + right
