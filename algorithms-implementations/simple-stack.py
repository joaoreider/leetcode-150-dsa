class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Poping from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peeking from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)