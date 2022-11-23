from collections import deque
class Queue:
    def __init__(self):
        self.buff = deque()
    
    def append(self,value):
        self.buff.appendleft(value)
        
    def pop(self):
        try:
            return self.buff.pop()
        except IndexError:
            return ('Error: Queue is empty')
            
    
    def size(self):
        return len(self.buff)

    def is_empty(self):
        return len(self.buff)==0
    
q = Queue()
q.append('this')
q.append('90')
q.append('stco myre')
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

print(q.size())
