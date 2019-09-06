class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items = self.items[1:]
    
    def size(self):
        return len(self.items)
    
    def first(self):
        return self.items[0]
    
    def contains(self, item):
        return item in self.items