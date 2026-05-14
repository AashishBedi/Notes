class Queue:
    def __init__(self):
        self.q = []
        
    def is_empty(self):
        return len(self.q) == 0
    
    def enqueue(self, data):
        self.q.append(data)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.q.pop(0)
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.q[0]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.q[-1]
    
    def size(self):
        return len(self.q)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.get_front())  # 10
print(q.get_rear())   # 30
print(q.size())       # 3
print(q.dequeue())   # 10
print(q.size())       # 2
