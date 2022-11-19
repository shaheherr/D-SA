from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def pop(self):
        return self.container.pop()
        
    def push(self,item):
        self.container.append(item)
        
    def peak(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

#problem1 --> reverse a string

def reverse_string():
    statement = ""
    #statement = input("Enter the string>>")
    state_stack = Stack()
    for word in  statement:
        state_stack.push(word)
    ret = str()
    for i in statement:
        ret +=  state_stack.pop()
    print(ret)

def is_match(c1,c2):
    match_dict = {
        '(':')',
        '[':']',
        '{':'}'
        }
    return match_dict[c1]==c2

#problem2 --> check for balanced paranthesis
def is_balanced(sample):
    stack2 = Stack()
    start = ['[','(',"{"]
    end = [']',')','}']
    for ch in sample:
        if ch in start:
            stack2.push(ch)
            continue
        if ch in end:
            if stack2.is_empty():
                return False
            if is_match(stack2.pop(),ch):
                continue
            else:
                return False
    
reverse_string()
print(is_balanced('(('))
