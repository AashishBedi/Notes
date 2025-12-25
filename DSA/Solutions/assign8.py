class Stack(list):
    # 2. Check if stack is empty
    def is_empty(self):
        return len(self) == 0

    # 3. Push element onto stack
    def push(self, data):
        self.append(data)

    # 4. Pop top element from stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return super().pop()

    # 5. Peek top element of stack
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self[-1]

    # 6. Return size of stack
    def size(self):
        return len(self)

    # 7. Restrict use of insert() method
    def insert(self, index, value):
        raise AttributeError("insert() method is not allowed in Stack")
