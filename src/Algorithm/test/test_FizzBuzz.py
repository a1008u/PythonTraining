import unittest
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

from src.Algorithm.FizzBuzz import Solution

class MyTestCase(unittest.TestCase):
    def test_fizzbuzz_v1(self):
        expects: List[str] = {"1", "2", "Fizz", "4", "Buzz", "FizzBuzz"}
        nums: List[int] = [1, 2, 3, 4, 5, 15]
        solution: Solution = Solution()
        results: List[str] = solution.fizzbuzz(nums)
        self.assertEqual(sorted(results), sorted(expects))


if __name__ == '__main__':
    unittest.main()
