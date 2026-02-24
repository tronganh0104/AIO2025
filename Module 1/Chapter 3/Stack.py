class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.capacity
    
    def push(self, value):
        if self.isFull():
            print("Stack is full")
        else:
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]
        
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.isFull())   # False
print(stack1.top())      # 2
print(stack1.pop())      # 2
print(stack1.top())      # 1
print(stack1.pop())      # 1
print(stack1.isEmpty())  # True