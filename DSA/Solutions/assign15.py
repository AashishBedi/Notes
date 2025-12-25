class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None
        
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start is None
    
    def push(self, item, priority):
        n = Node(item, priority)
        
        #Case 1: Empty Queue or new node has higher priority than start
        if self.start is None or self.start.priority < priority:
            n.next = self.start
            self.start = n
        else:
            #Traverse to find correct position
            temp = self.start
            while temp.next is not None and temp.next.priority >= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("PQ is empty")
        
        temp = self.start
        self.start = self.start.next
        self.item_count -= 1
        return temp.item
    
    def size(self):
        return self.item_count

if __name__ == "__main__":
    pq = PriorityQueue()

    pq.push("Low", 1)
    pq.push("Medium", 3)
    pq.push("High", 5)
    pq.push("Medium-High", 4)

    print("Size:", pq.size())          # 4
    print("Pop:", pq.pop())            # High
    print("Pop:", pq.pop())            # Medium-High
    print("Size:", pq.size())          # 2