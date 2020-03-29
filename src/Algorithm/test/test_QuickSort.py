import unittest
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

from Algorithm.QuickSort import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums: List[int] = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
        nums2: List[int] = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
        solution: Solution = Solution()
        results: List[int] = solution.quick_sort(nums)

        self.assertEqual(sorted(nums2), results)

    def test_something2(self):
        nums: List[int] = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
        nums2: List[int] = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
        solution: Solution = Solution()
        results: List[int] = solution.quick_sort2(nums)

        self.assertEqual(sorted(nums2), results)


if __name__ == '__main__':
    unittest.main()
