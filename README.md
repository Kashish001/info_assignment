# Calendar Program Issues

## Issues
- Node.insert Method was not handling a condition for overlapping. which result in double booking of the events.
-Tree structure was not managed perfectly, that causes incorrect placement of nodes/events.

## How code was Debugged
1. Implement logic for checking the overlapping of events.
2. check for inserting the event was not properly implemented `node.start >= self.end` then we have to insert it in right child and return statement was also wrong as it was as follow `return self.left_child.insert(node)` while thew check was for right child.
3. similarly for left child check should be `node.end <= self.start`.
4.`return self.root.insert(node=Node(start, end))` here we were passing keyword argument(kwargs) to the `Node.insert` method while it was expecting a single argument.
