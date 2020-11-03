from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def comb_sort(self, nums: List[int]) -> List[int]:

        '''
        comb_sortの説明
        gapを利用して、ソートをかける。

        BubbleSortの改良

        対象データ: 2,1,5,8,7,3

        - 1回目: 2,1,5,8,7,3 swap=false　gap: 4 = 6/ 1.3
        - 2回目: 2,1,3,8,7,5 swap=false　gap: 3 = 4/ 1.3
        - 3回目: 2,1,3,5,7,8 swap=false　gap: 2 = 3/ 1.3
        - 4回目: 1,2,3,5,7,8 swap=false　gap: 1 = 2/ 1.3
        - 5回目: 1,2,3,5,7,8 swap=true    gap: 1
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
