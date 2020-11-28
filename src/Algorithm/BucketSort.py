# coding: utf-8
from typing import List

# from Algorithm.StopWatch import stop_watch
from src.Algorithm import InsertionSort
from src.Algorithm.StopWatch import stop_watch

class Solution:
    """
    bubble sortのイメージ
    対象データ: 2,1,5,8,7,3
    - 最大値：8

    ### まずはbuckets(2次元配列)に分けましょう
    - index:0の入れ物[2,1,5,3]
    - index:1の入れ物[8,7]
    - index:2の入れ物[]
    - index:3の入れ物[]
    - index:4の入れ物[]
    - index:5の入れ物[]

    ### こちらでInsertion Sortを実行
    - index:0の入れ物[2,1,5,3]
        → 1 | 2, 5, 3  → 1 ,2 |  5, 3 →  1 ,2, 3 | 5 → 1,2,3,5
    - index:1の入れ物[8,7] -> 7 | 8 -> 7,8
    """

    @stop_watch
    def bucket_sort(self, nums: List[int]) -> List[int]:

        max_num: int = max(nums)
        size: int = 6

        # bucketsへsort対象の値を分ける
        buckets: List[List[int]] = [[] for _ in range(size)]
        for num in nums:
            i = num // size
            if i != size:
                buckets[i].append(num)
            else:
                buckets[size - 1].append(num)

        print(buckets)

        solution: InsertionSort.Solution = InsertionSort.Solution()
        for i in range(size):
            solution.insertion_sort(buckets[i])

        result: List[int] = []
        for i in range(size):
            result += buckets[i]

        return result
