class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.capacity
    
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.queue.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.queue.pop(0)
        
    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.queue[0]

queue1 = MyQueue(capacity=5)

queue1.enqueue(10)
queue1.enqueue(20)

print(queue1.front())    # 10
print(queue1.dequeue())  # 10
print(queue1.front())    # 20
print(queue1.dequeue())  # 20
print(queue1.isEmpty())  # True