class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self, data):
        n = Node(data)
        
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        removed_data = self.front.data
        self.front = self.front.next
        self.item_count -= 1
        
        if self.front is None:
            self.rear = None
        return removed_data
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.data
    
    def size(self):
        return self.item_count

if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front:", q.get_front())     # 10
    print("Rear:", q.get_rear())       # 30
    print("Size:", q.size())           # 3

    print("Dequeued:", q.dequeue())    # 10
    print("Front after dequeue:", q.get_front())  # 20
    print("Size:", q.size())           # 2