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
    
s = Queue() 

def count_parentheses(file,left_sym,right_sym):
    index=0
    for line in file:  
        for token in line:
            if token in left_sym:  
                s.queue(token)  
            elif token in right_sym:  
                if s.is_empty():  
                    pass 
                else:  
                    left = s.dequeue()
                    index +=1
                    if (token == right_sym and left != left_sym):
                        pass
    print(left_sym+right_sym+' pairs: '+str(index))
    return s.is_empty()

def match_parentheses(file,left_sym,right_sym):  
    matching=True
    for line in file:  
        for token in line:
            if token in left_sym:  
                s.queue(token)  
            elif token in right_sym:  
                if s.is_empty():  
                    print('Not all '+left_sym+right_sym+' matched.')
                    matching= False
                else:  
                    left = s.dequeue()
                    if (token == right_sym and left != left_sym):
                        print('Not all '+left_sym+right_sym+' matched.')
                        matching= False
    if matching and s.is_empty():
        print('All '+left_sym+right_sym+' matched.')
    else:
        return False
    return s.is_empty()    
    
def main():        
    # read  file  
    filename=input('Enter the file name: ')
    my_file = open(filename, 'r').readlines()        
    for line in my_file:          
        line.strip() 
    count_parentheses(my_file,'(',')')
    count_parentheses(my_file,'{','}')
    count_parentheses(my_file,'[',']')
    match_parentheses(my_file,'(',')')
    match_parentheses(my_file,'{','}')
    match_parentheses(my_file,'[',']')
main()
    
