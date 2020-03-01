import unittest
import sys
sys.path.append('/root/src/')
print(sys.path)
print(dir())

from LongestCommonPrefix.longestcommonprefix import Solution

class MyTestCase(unittest.TestCase):
    def test_something_v1(self):

        expect: str = "fl"
        strs: List[str] = ["flower", "flow", "flight"]

        solution: Solution = Solution()
        result: str = solution.longestCommonPrefix(strs)
        self.assertEqual(result, expect)

    def test_something_v2(self):

        expect: str = ""
        strs: List[str] = ["c", "acc", "ccc"]

        solution: Solution = Solution()
        result: str = solution.longestCommonPrefix(strs)
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()
