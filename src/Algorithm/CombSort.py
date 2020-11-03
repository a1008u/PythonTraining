from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def comb_sort(self, nums: List[int]) -> List[int]:

        '''
        comb_sortの説明
        swapを利用して変更があったか目印（印）を利用し、
        対象データを-> , <-の流れで入れ替えていく。

        BubbleSortの改良

        対象データ: 2,1,5,8,7,3 swap=false

        - 1回目→: 1,2,5,3,7 | 8 swap=true
        - 2回目←: 1,2,3,5 | 7,8 swap=true
        - 3回目→: 1,2,3 | 5,7,8 swap=false
        '''

        len_nums: int = len(nums)
        gap: int = len_nums
        swapped: bool = True

        while gap != 1 or swapped:
            gap = int(gap / 1.3)
            if gap < 1:
                gap = 1

            swapped = False

            for i in range(0, len_nums - gap):
                if nums[i] > nums[gap + i]:
                    nums[i], nums[gap + i] = nums[gap + i], nums[i]
                    swapped = True
        return nums
