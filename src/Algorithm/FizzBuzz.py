# coding: utf-8
from typing import List

class Solution:
    def fizzbuzz(self, nums: List[int]) -> List[str]:
        results: List[str] = []
        for index, num in enumerate(nums):
            if num % 3 == 0 and num % 5 == 0:
                results.append("FizzBuzz")
                continue
            if num % 3 == 0:
                results.append("Fizz")
                continue
            if num % 5 == 0:
                results.append("Buzz")
                continue
            results.append(str(num))
        return results
