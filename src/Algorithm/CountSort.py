# coding: utf-8
from typing import List

from src.Algorithm.StopWatch import stop_watch


class Solution:

    @stop_watch
    def count_sort(self, nums: List[int]) -> List[int]:

        '''
        Shell_Sortの説明
        事前にGAPを決めて、そちらを使って一定の区間でsortをしていく
        ＊Insertion sortの改良

        対象データ: 2,1,5,8,7,3

        ### 準備
        - [0, 1, 1, 1, 0, 1, 0, 1, 1] -> 最大値と同じ値の配列を作成して、個数をカウント
        - [0, 1, 2, 3, 3, 4, 4, 5, 6] -> 対象インデックスの個数と前のインデックスの個数を足す

        ### sort
        - 1回目: [,,,,,8] -> 2,1,5,8,7,3の8の値をを確認する -> 5番目とわかる ->  [0, 1, 2, 3, 3, 4, 4, 5, 5]の対象の値を-1する。
        - 2回目: [,,,,7,8] -> 2,1,5,8,7,3の7の値をを確認する -> 4番目とわかる ->  [0, 1, 2, 3, 3, 4, 4, 4, 5]の対象の値を-1する。
        - 3回目: [,,,5,7,8] -> 2,1,5,8,7,3の5の値をを確認する -> 3番目とわかる ->  [0, 1, 2, 3, 3, 3, 4, 4, 5]の対象の値を-1する。
        - 4回目: [,,3,5,7,8] -> 2,1,5,8,7,3の3の値をを確認する -> 2番目とわかる ->  [0, 1, 2, 2, 3, 4, 4, 4, 5]の対象の値を-1する。
        - 5回目: [,2,3,5,7,8] -> 2,1,5,8,7,3の2の値をを確認する -> 1番目とわかる ->  [0, 0, 2, 2, 3, 4, 4, 4, 5]の対象の値を-1する。
        - 6回目: [1,2,3,5,7,8] -> 2,1,5,8,7,3の1の値をを確認する -> 0番目とわかる ->  [0, 0, 2, 2, 3, 4, 4, 4, 5]の対象の値を-1する。
        '''

        max_num: int = max(nums)
        counts: List[int] = [0] * (max_num + 1)
        result: List[int] = [0] * len(nums)

        for num in nums:
            counts[num] += 1

        for i in range(1, len(counts)):
            counts[i] += counts[i-1]

        i: int = len(nums) - 1
        while i >= 0:
            index: int = nums[i]
            result[counts[index]-1] = nums[i]
            counts[index] -= 1
            i -= 1

        return result
