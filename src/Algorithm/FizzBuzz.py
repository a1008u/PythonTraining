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

    def threefive(self, nums) -> str:
        for num in nums:
            if type(num) == int and num % 3 == 0 and num % 5 == 0:
                yield "FizzBuzz"
                continue
            yield num

    def three(self, nums) -> str:
        for num in nums:
            if type(num) == int and num % 3 == 0:
                yield "Fizz"
                continue
            yield num

    def five(self, nums) -> str:
        for num in nums:
            if type(num) == int and num % 5 == 0:
                yield "Buzz"
                continue
            yield num

    def notChange(self, nums) -> str:
        for num in nums:
            yield str(num)

    def fizzbuzz_yieldV1(self, nums: List[int]) -> List[str]:
        return list(num for num in self.notChange(self.five(self.three(self.threefive(nums)))))

    def generatorV2(self, nums) -> str:
        for index, num in enumerate(nums):
            if num % 3 == 0 and num % 5 == 0:
                yield "FizzBuzz"
                continue
            if num % 3 == 0:
                yield "Fizz"
                continue
            if num % 5 == 0:
                yield "Buzz"
                continue
            yield str(num)

    def fizzbuzz_yieldV2(self, nums: List[int]) -> List[str]:
        return list(num for num in self.generatorV2(nums))
