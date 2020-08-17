#python3

#implementation of min stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]
    
    def push(self,x) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
