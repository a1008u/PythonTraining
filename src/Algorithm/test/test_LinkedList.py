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

        results.reverse_iterative()
        expectsreverse: List[int] = [2, 1, 5]

        self.assertEqual(expectsreverse[0], results.head.data)
        self.assertEqual(expectsreverse[1], results.head.next.data)
        self.assertEqual(expectsreverse[2], results.head.next.next.data)

        results.reverse_recursive()
        expectsreverse2: List[int] = [5, 1, 2]

        self.assertEqual(expectsreverse2[0], results.head.data)
        self.assertEqual(expectsreverse2[1], results.head.next.data)
        self.assertEqual(expectsreverse2[2], results.head.next.next.data)

        results2: LinkedList = LinkedList()
        results2.append(2)
        results2.append(4)
        results2.append(6)
        results2.append(1)
        results2.append(2)
        results2.append(4)
        results2.append(6)
        expectsreverse3: List[int] = [6,4,2,1,6,4,2]

        results2.reverse_even()
        self.assertEqual(expectsreverse3[0], results2.head.data)
        self.assertEqual(expectsreverse3[1], results2.head.next.data)
        self.assertEqual(expectsreverse3[2], results2.head.next.next.data)
        self.assertEqual(expectsreverse3[3], results2.head.next.next.next.data)
        self.assertEqual(expectsreverse3[4], results2.head.next.next.next.next.data)
        self.assertEqual(expectsreverse3[5], results2.head.next.next.next.next.next.data)
        self.assertEqual(expectsreverse3[6], results2.head.next.next.next.next.next.next.data)



if __name__ == '__main__':
    unittest.main()


