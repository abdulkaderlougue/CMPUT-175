import time

class BoundedQueue:
    # Constructor, which creates a new empty queue, with user-specified capacity:
    def __init__(self, capacity):
        if type(capacity) is not int or capacity<=0:
            raise(Exception('capacity is not a positive integer'))  
        else:
            self.elements = [ ]
            self.itemMax = capacity     
       
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        # MazeSquare
        if (len(self.elements) == self.itemMax):
            raise(Exception('The queue is full'))
        else:
            self.elements.append(item)
        return None
       
    # Removes and returns the front-most item in the queue. 
    # Returns nothing if the queue is empty.
    def dequeue(self):
        if len(self.elements) == 0:
            raise(Exception('The queue is empty'))
        else:
            x = self.elements[0]
            del self.elements[0]
            return x
       
    # Returns the front-most item in the queue, and DOES NOT change the queue. 
    def peek(self):
        if len(self.elements) == 0:
            raise(Exception('The queue is empty'))
        else:
            return self.elements[0]
    # Returns True if the queue is empty, and False otherwise:
    def is_empty(self):
        # MazeSquare
        return self.elements == []
    # Returns True if the queue is full, and False otherwise:
    def is_full(self):
        # MazeSquare
        return (len(self.elements) == self.itemMax)
    # Returns the number of items in the queue:
    def size(self):
        # MazeSquare
        return len(self.elements)
    # Returns the capacity of the queue:
    def capacity(self):
        # MazeSquare
        return self.itemMax
    # Removes all items from the queue, and sets the size to 0.
    # clear() should not change the capacity
    def clear(self):
        # MazeSquare
        self.elements = []
    # Returns a string representation of the queue:
    def __str__(self):
        string = ''.join(self.elements)
        return string         
    
class CircularQueue:
    def __init__(self,capacity):
        if  type(capacity) != int or capacity<=0:
            raise Exception('Capacity Error')                
        self.__items = []
        self.__capacity = capacity
        self.__count = 0
        self.__head = 0
        self.__tail = 0
     
    def enqueue(self,item):
        if  type(self.__capacity) != int or self.__capacity<=0:
            raise Exception('Capacity Error') 
        if len(self.__items) < self.__capacity:
            self.__items.append(item)  
        else:
            self.__items[self.__tail] = item
        self.__count += 1
        self.__tail = (self.__tail + 1)%self.__capacity
        
        
        # Removes and returns the front most item in the queue.      
        # Returns nothing if the queue is empty.        
    def dequeue(self,item):
        if  type(self.__capacity) != int or self.__capacity<=0:
            raise Exception('Capacity Error')         
        item = self.__items[self.__head]
        self.__items[self.__head]= None
        self.__count -= 1
        self.__head = (self.__head+1) % self.__capacity  
        return item
        
        
    def peek(self):
        if  type(capacity) != int or capacity<=0:
            raise Exception('Capacity Error')   
        
        return self.__items[self.__head]        
    
    def isEmpty(self):
        return self.__count == 0
    
    def isFull(self):
        return self.__count == self.__capacity
    
    def size(self):
        return self.__count
    
    def capacity(self):
        return self.__capacity
    
    def clear(self):
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0        
        
    def elements(self):
        return self.__items
    
    def __str__(self):
        str_exp = "]"        
        i=self.__head
        for j in range(self.__count):            
            str_exp += str(self.__items[i]) + " "                   
            i=(i+1) % self.__capacity
        return str_exp + "]" 
    
    def __repr__(self): 
        return str(self.__items) + " H=" + str(self.__head) + " T="+str(self.__tail) + " (" +str(self.__count)+"/"+str(self.__capacity)+")"
    
    
def main():
    bQueue = BoundedQueue(10000)
    cQueue = CircularQueue(10000)
    for i in range (0, 10000):
        bQueue.enqueue(i)
    for i2 in range (0,10000):
        cQueue.enqueue(i)
        
    start__b = time.time()
    for i3 in range (0,10000):
        bQueue.dequeue()
    end__b = time.time()
    
    time__b = end__b-start__b
    
    start__c = time.time()
    for i3 in range (0,10000):
        cQueue.dequeue(i3)
    end__c = time.time()
        
    time__c = end__c-start__c   
    
    print(time__b)
    print(time__c)

main()