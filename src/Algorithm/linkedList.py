from typing import Any

class Node:
    def __init__(self, data:Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: Any):
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node:Node = self.head
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
