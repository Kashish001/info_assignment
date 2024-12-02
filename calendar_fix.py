#!/usr/bin/python3

from typing import Optional, Self

class Node():
    def __init__(self: Self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        #Overlapping condition check
        if node.end > self.start and node.start < self.end:
            return False
        #check was wrong we need a right child if new event start time
        #is greater than or equal to current event end time
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            # Here we need to insert in right child not left
            return self.right_child.insert(node)
        #similarly check was wrong we need a left child if new event end time
        #is less than or equal to current event start time
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)

class Calendar():
    def __init__(self: Self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        #root.insert is expecting a single argument of type Node
        #but we are passing keyword argument
        return self.root.insert(Node(start, end))


calendar = Calendar()
print(calendar.book(5, 10))
print(calendar.book(8, 13))
print(calendar.book(10, 15))
