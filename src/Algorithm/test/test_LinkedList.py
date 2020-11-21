import unittest
import sys, os
from typing import List

print('prepare test start-----------------------')
path = os.path.join(os.path.dirname(__file__), '../../../')
sys.path.append(path)
sys.path.append('/root/src/')
print(sys.path)
print(dir())
print('prepare test end-----------------------')

from src.Algorithm.linkedList import LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        results: LinkedList = LinkedList()
        results.append(1)
        results.append(2)
        results.append(3)
        expects: List[int] = [1, 2, 3]

        self.assertEqual(expects[0], results.head.data)
        self.assertEqual(expects[1], results.head.next.data)
        self.assertEqual(expects[2], results.head.next.next.data)

        results.remove(3)
        self.assertIsNone(results.head.next.next)

        results.insert(5)
        self.assertEqual(5, results.head.data)


if __name__ == '__main__':
    unittest.main()


