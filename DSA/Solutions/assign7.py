class Stack:
    def __init__(self):
        self.s = []
    
    def is_empty(self):
        return len(self.s) == 0
    
    def push(self, data):
        self.s.append(data)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.s.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.s[-1]
    
    def size(self):
        return len(self.s)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())     # 30
print(s.pop())      # 30
print(s.size())     # 2
print(s.is_empty()) # False