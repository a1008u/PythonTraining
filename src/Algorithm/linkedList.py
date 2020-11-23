from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList:

    """
    - 下記のような形として登録される。
    - HEAD -> data|next -> data|next -> data|next -> None
    """

    def __init__(self) -> None:
        self.head = None

    def append(self, data: Any):
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node: Node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node: Node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node: Node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any):
        current_node: Node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node: Node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self) -> None:
        """
        [1,2,3] -> [3,2,1]に変換する

        """
        previous_node: Node = None
        current_node: Node = self.head
        while current_node:
            next_node: Node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node: Node, preious_node: Node) -> None:
            if not current_node:
                return preious_node

            next_node: Node = current_node.next
            current_node.next = preious_node
            preious_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, preious_node)
        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> None:
        """
        連続する偶数のみを反転する
        1,4,6,8,9 -> 1,8,6,4,9
        1,2,3,4,5 -> 1,2,3,4,5
        :return:
        """
        def _reverse_even(head: Node, previous_node: Node) -> Optional[Node]:

            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node: Node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)
