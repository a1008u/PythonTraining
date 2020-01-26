# coding: utf-8
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        resultIndex1: int = 0
        resultIndex2: int = 0
        # for index, num in enumerate(nums):
        #     for i in range(len(nums)):
        #         if i != index and i - index > 0:
        #             if target == num + nums[i]:
        #                 resultIndex1 = index
        #                 resultIndex2 = i

        i: int = 0
        while i < len(nums):
            if i == len(nums) - 1:
                break
            wanted = target - nums[i]
            rest = nums[i+1:]
            if wanted in rest:
                resultIndex1 = i
                resultIndex2 = rest.index(wanted) + i + 1
                break
            i = i+1

        return [resultIndex1, resultIndex2]

    def twoSumDict(self, nums: List[int], target: int) -> List[int]:

        resultIndex1: int = 0
        resultIndex2: int = 0

        dic: dict = {}
        for index, num in enumerate(nums):
            dic[num] = index

        for index, num in enumerate(nums):
            wantedValue = target - num
            if dic.get(wantedValue) and index != dic.get(wantedValue):
                resultIndex1 = index
                resultIndex2 = dic.get(wantedValue)
                break

        return [resultIndex1, resultIndex2]

    def twoSumDictOnePass(self, nums: List[int], target: int) -> List[int]:

        resultIndex1: int = 0
        resultIndex2: int = 0

        dic: dict = {}
        for index, num in enumerate(nums):
            wantedValue = target - num
            if None != dic.get(wantedValue) and index != dic.get(wantedValue):
                resultIndex1 = dic.get(wantedValue)
                resultIndex2 = index
                break
            dic[num] = index
        return [resultIndex1, resultIndex2]
