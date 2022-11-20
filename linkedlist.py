class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_end(self,newnode):
        if self.head == None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next == None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newnode
            
n = Node('John')
l = LinkedList()
l.insert_end(n)
