from typing import List

from src.Algorithm.StopWatch import stop_watch

@stop_watch
class Solution:

    def cocktail_sort(self, nums: List[int]) -> List[int]:

        len_nums: int = len(nums)
        swapped: bool = True
        start: int = 0
        end: int = len_nums - 1

        while swapped:
            swapped = False
            for i in range(start, end):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True

            start += 1

        return nums
