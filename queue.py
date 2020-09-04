class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def isEmpty(self):
        return self.head is None
    def peek(self):
        return self.head.data if self.head is not None else None
    def add(self, data):
        node = self.Node(data)
        if(self.tail is not None):
            self.tail.next = node
        self.tail = node
        if (self.head is None):
            self.head = node
    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if (self.head is None):
            self.tail = None
        return data
        