class Stack:
    def __init__(self):
        self.top = None
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def isEmpty(self):
        return self.top is None
    def peek(self):
        return self.top.data if self.top is not None else None
    def push(self,data):
        node = self.Node(data)
        node.next = self.top
        self.top = node
    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data
