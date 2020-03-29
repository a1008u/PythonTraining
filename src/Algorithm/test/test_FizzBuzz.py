import unittest
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

from src.Algorithm.FizzBuzz import Solution

class MyTestCase(unittest.TestCase):
    def test_fizzbuzz_v1(self):
        expects: List[str] = {"1", "2", "Fizz", "4", "Buzz", "FizzBuzz", "22"}
        nums: List[int] = [1, 2, 3, 4, 5, 15, 22]
        solution: Solution = Solution()
        results: List[str] = solution.fizzbuzz(nums)
        self.assertEqual(sorted(results), sorted(expects))

    def test_fizzbuzz_yield_v1(self):
        expects: List[str] = {"1", "2", "Fizz", "4", "Buzz", "FizzBuzz", "22"}
        nums: List[int] = [1, 2, 3, 4, 5, 15, 22]
        solution: Solution = Solution()
        results: List[str] = solution.fizzbuzz_yieldV1(nums)
        self.assertEqual(sorted(expects), sorted(results))

    def test_fizzbuzz_yield_v2(self):
        expects: List[str] = {"1", "2", "Fizz", "4", "Buzz", "FizzBuzz", "22"}
        nums: List[int] = [1, 2, 3, 4, 5, 15, 22]
        solution: Solution = Solution()
        results: List[str] = solution.fizzbuzz_yieldV2(nums)
        self.assertEqual(sorted(expects), sorted(results))

if __name__ == '__main__':
    unittest.main()
