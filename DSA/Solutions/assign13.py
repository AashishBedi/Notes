class Node:
    def __init__(self, item):
        self.prev = None
        self.item = item
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.item_count += 1
    
    def insert_rear(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = self.rear = n
        else:
            self.rear.next = n
            n.prev = self.rear
            self.rear = n
        self.item_count += 1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        data = self.front.item
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
        return data
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.rear.item
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
        return data
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.item
    
    def size(self):
        return self.item_count


if __name__ == "__main__":
    d = Deque()

    d.insert_front(10)
    d.insert_rear(20)
    d.insert_front(5)

    print("Front element:", d.get_front())
    print("Rear element:", d.get_rear())
    print("Deque size:", d.size())

    print("Deleted front:", d.delete_front())
    print("Deleted rear:", d.delete_rear())
    print("Deque size after deletions:", d.size())