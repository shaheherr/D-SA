class Hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]
        
    def hashing(self,key):
        summ = 0
        summ = sum([ord(letter) for letter in key])
        return summ % 100
    
    def __setitem__(self,key,value):
        found = False
        h = self.hashing(key)
        for idx,val in enumerate(self.arr[h]):
            if len(val)==2 and val[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
            
    def __getitem__(self,key):
        h = self.hashing(key)
        for element in self.arr[h]:
            if key == element[0]:
                return element[1]
            
    def __delitem__(self,key):
        h = self.hashing(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]
t = Hashmap()
t['march 6'] = 455
t['6 march'] = 67
t['feb 7'] = 87
del t['6 march']
print(t['6 march'])
