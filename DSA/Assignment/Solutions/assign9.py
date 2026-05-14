from assign3 import SLL

class Stack:
    def __init__(self):
        # Create Singly Linked List object
        self.sll = SLL()

    def is_empty(self):
        return self.sll.is_empty()

    def push(self, data):
        # Push = insert at start
        self.sll.insert_at_start(data)

    def pop(self):
        # Pop = delete first node
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.sll.delete_first()

    def peek(self):
        # Return top element
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.sll.get_first()

    def size(self):
        return self.sll.size()

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Top element:", s.peek())     # 30
    print("Stack size:", s.size())       # 3
    print("Popped:", s.pop())            # 30
    print("Stack size:", s.size())       # 2
