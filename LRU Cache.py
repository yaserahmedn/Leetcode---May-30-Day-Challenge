#Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
#get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
#The cache is initialized with a positive capacity.


class LRUCache:
    priorityQueue=list()

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.priorityQueue=[None]*capacity
        

    def get(self, key: int) -> int:
        
        for tuples in self.priorityQueue:
            if tuples is not None:
                if tuples[0]==key:
                    ind=self.priorityQueue.index(tuples)
                    found=self.priorityQueue.pop(ind)
                    self.priorityQueue.append(found)
                    return found[1]
        
        return -1


    def put(self, key: int, value: int) -> None:
        
        if(len(self.priorityQueue)>self.capacity):
            flag=False
            for tuples in self.priorityQueue:
                if tuples is not None:
                    if tuples[0]==key:
                        tuples[1]=value
                        ind=self.priorityQueue.index(tuples)
                        found=self.priorityQueue.pop(ind)
                        self.priorityQueue.append(found)
                        flag=True
                        break
            if flag==False:
                self.priorityQueue.append([key,value])
        
        
        elif(len(self.priorityQueue)==self.capacity):
            flag=False
            for tuples in self.priorityQueue:
                if tuples is not None:
                    if tuples[0]==key:
                        tuples[1]=value
                        ind=self.priorityQueue.index(tuples)
                        found=self.priorityQueue.pop(ind)
                        self.priorityQueue.append(found)
                        flag=True
                        break
            if flag==False:
                self.priorityQueue.pop(0)
                self.priorityQueue.append([key,value])
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
