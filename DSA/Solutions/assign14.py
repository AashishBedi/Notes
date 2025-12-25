class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def is_empty(self):
        return len(self.pq) == 0
    
    def push(self, data, priority):
        self.pq.append((priority, data))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("PQ is empty")
        
        #Find index of high priority element
        max_idx = 0
        for i in range(1, len(self.pq)):
            if self.pq[i][0] > self.pq[max_idx][0]:
                max_idx = i
        return self.pq.pop(max_idx)[1]
    
    def size(self):
        return len(self.pq)

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.push("Low priority task", 1)
    pq.push("Medium priority task", 3)
    pq.push("High priority task", 5)

    print("Size:", pq.size())           # 3
    print(pq.pop())                     # High priority task
    print("Size:", pq.size())           # 2
    print("Is Empty:", pq.is_empty())   # False