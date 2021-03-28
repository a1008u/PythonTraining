from typing import List, NewType

from src.Algorithm.StopWatch import stop_watch

IndexNum = NewType('IndexNum', int)


class Solution:

    @stop_watch
    def linear_seach(self, nums: List[int], value: int) -> IndexNum:
        for i in range(0, len(nums)):
            if nums[i] == value:
                return i
        return -1

    @stop_watch
    def binary_search(self, nums: List[int], value: int) -> IndexNum:
        """
        対象データ: 1,2,3,4,5,7,8 value:2

        - 1回目: 1,2,3,4,5,7,8 mid:4 value:2 → midより小さい
        - 2回目: 1,2,3 mid:2 value:2 -> 一致
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == value:
                return mid
            elif nums[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @stop_watch
    def binary_search2(self, nums: List[int], value: int) -> IndexNum:
        def _binary_search(
                nums: List[int], value: int, left: IndexNum, right: IndexNum) -> IndexNum:
            if left > right:
                return -1

            mid: int = (left + right) // 2
            if nums[mid] == value:
                return mid
            elif nums[mid] < value:
                return _binary_search(nums, value, mid + 1, right)
            else:
                return _binary_search(nums, value, left, mid - 1)

        return _binary_search(nums, value, 0, len(nums) - 1)
