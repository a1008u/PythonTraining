from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def cocktail_sort(self, nums: List[int]) -> List[int]:

        '''
        cocktail_sortの説明
        swapを利用して変更があったか目印（印）を利用し、
        対象データを-> , <-の流れで入れ替えていく。

        BubbleSortの改良

        対象データ: 2,1,5,8,7,3 swap=false

        - 1回目→: 1,2,5,3,7 | 8 swap=true
        - 2回目←: 1,2,3,5 | 7,8 swap=true
        - 3回目→: 1,2,3 | 5,7,8 swap=false
        '''

        len_nums: int = len(nums)
        swapped: bool = True
        start: int = 0
        end: int = len_nums - 1

        while swapped:
            swapped = False

            # -> 向きの処理
            for i in range(start, end):
                swapped = self.change(i, nums)

            if not swapped:
                break

            swapped = False
            end -= 1

            # <- 向きの処理
            for i in range(end - 1, start - 1, -1):
                swapped = self.change(i, nums)

            start += 1

        return nums

    @staticmethod
    def change(i, nums):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return True
