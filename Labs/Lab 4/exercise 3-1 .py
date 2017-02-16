class Queue:
    
    # Constructor, which creates a new empty queue:
    def __init__(self):
        self.items=[]
        # TODO: You must implement this constructor!
        
    # Adds a new item to the back of the queue, and returns nothing:
    def queue(self, item):
        self.items.insert(0,item)
        return self.items
        
        # TODO: You must implement this method!
        
    # Removes and returns the front-most item in the queue.  
    # Returns nothing if the queue is empty.
    def dequeue(self):
        if Queue.size(self) == 0:
            return None        
        else:
            return self.items.pop()
             
        # TODO: You must implement this method!
        
    # Returns the front-most item in the queue, and DOES NOT change the queue.  
    def peek(self):
        if Queue.size(self) == 0:
            return None
        else:
            return self.items[len(self.items)-1]        
        # TODO: You must implement this method!
        
    # Returns True if the queue is empty, and False otherwise:
    def is_empty(self):
        return self.items == []
        # TODO: You must implement this method!
    
    # Returns the number of items in the queue:
    def size(self):
        return len(self.items)
        # TODO: You must implement this method!
    
    # Removes all items from thq queue, and sets the size to 0:
    def clear(self):
        self.items = []
        # TODO: You must implement this method!
        
    # Returns a string representation of the queue:
    def __str__(self):
        return repr(self.items)
        # TODO: You must implement this method!
    
q=Queue()
choose=input( 'Add ,Serve, or Exit:')
while choose!= "Exit":
    if choose=="Serve":        
        if q.is_empty():
            
            print('The lineup is already empty.')
        else:
            print(q.dequeue(),"has been served")
    elif choose == "Add":
        if q.size() ==3:
            print("You cannot add more people, the lineup is full!")
        else:
            add=input("Enter the name of the person to add:")
            q.queue(add)
    else:
        print("invalid command...")
    choose= input("Add, Serve, or Exit:")
    
        