class heap():
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while idx > 0 and \
              self.heap[(idx - 1) // 2] < self.heap[idx]:
            self.heap[(idx - 1) // 2], self.heap[idx] =\
            self.heap[idx], self.heap[(idx - 1) // 2]
            idx = (idx - 1) // 2
            
            
    def extract(self):
        print(self.heap[0])
        self.heap[0] = self.heap[-1]
        idx = 0
            

        while 2 * idx + 2 < len(self.heap):
            max_idx = 2 * idx + 1 
            if self.heap[max_idx + 1] > self.heap[max_idx]:
                max_idx += 1    
                
            if self.heap[idx] < self.heap[max_idx]:
                self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
                idx = max_idx
            else:
                break
            

        self.heap.pop()
        

h = heap()
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == '0':
        h.insert(int(command[1]))
    else:
        h.extract()
