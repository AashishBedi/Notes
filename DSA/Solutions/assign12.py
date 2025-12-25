class Deque:
    def __init__(self):
        # Create an empty list as instance member
        self.items = []

    def is_empty(self):
        # Check if deque is empty
        return len(self.items) == 0

    def insert_front(self, data):
        # Insert element at front end
        self.items.insert(0, data)

    def insert_rear(self, data):
        # Insert element at rear end
        self.items.append(data)

    def delete_front(self):
        # Remove front element
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def delete_rear(self):
        # Remove rear element
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def get_front(self):
        # Return front element
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]

    def get_rear(self):
        # Return rear element
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]

    def size(self):
        # Return number of elements in deque
        return len(self.items)


if __name__ == "__main__":
    dq = Deque()

    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)

    print("Front:", dq.get_front())   # 5
    print("Rear:", dq.get_rear())     # 20
    print("Size:", dq.size())         # 3

    dq.delete_front()
    dq.delete_rear()

    print("Size after deletions:", dq.size())  # 1
