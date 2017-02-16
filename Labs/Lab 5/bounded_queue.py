class BoundedQueue:
    
    # Constructor, which creates a new empty queue, with user-specified capacity:
    def __init__(self, capacity):
        if type(capacity) is not int or capacity <0:
            raise (Exception('capacity is not a positive integer'))
        else:
            self.elements =[ ]
            self.itemMax = capacity
        
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        # TODO: You must implement this method!
        if (len(self.elements) == self.itemMax):
            raise (Exception('The queue is full'))
        else:
            self.elements.append(item)
        return None
    
    # Removes and returns the front-most item in the queue.  
    # Returns nothing if the queue is empty.
    def dequeue(self):
        if len(self.elements) == 0 :
            raise(Exception('The queue is empty'))
        else:
            x = self.elements[0]
            del self.elements[0]
            return x
        
    # Returns the front-most item in the queue, and DOES NOT change the queue.  
    def peek(self):
        # TODO: You must implement this method!
        if len(self.elements)==0 :
            raise(Exception('The queue is empty'))
        else:
            return self.elements[0]
        
        
    # Returns True if the queue is empty, and False otherwise:
    def is_empty(self):
        # TODO: You must implement this method!
        return self.elements == []
    
    # Returns True if the queue is full, and False otherwise:
    def is_full(self):
        # TODO: You must implement this method!
        return len(self.elements)== self.itemMax
    
    # Returns the number of items in the queue:
    def size(self):
        # TODO: You must implement this method!
        return len(self.elements)
    
    # Returns the capacity of the queue:
    def capacity(self):
        # TODO: You must implement this method!
        return self.itemMax
    
    # Removes all items from the queue, and sets the size to 0.
    # clear() should not change the capacity
    def clear(self):
        # TODO: You must implement this method!
        self.element = []
    
    # Returns a string representation of the queue:
    def __str__(self):
        # TODO: You must implement this method!
        string = ''.join(self.elements)
        return string   
    
# use this function to test your Bounded Queue implementation    
def test():
    is_pass = True

    try:
        string_queue = BoundedQueue('wrong type')
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"
    
    try:
        string_queue = BoundedQueue(-1)
    except Exception as e:
        is_pass = True
    else:
        is_pass = False  
    assert is_pass == True, "fail the test" 
        
    string_queue = BoundedQueue(3)
    
    is_pass = (string_queue.size() == 0)
    assert is_pass == True, "fail the test"
    
    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test" 
    
    is_pass = (string_queue.is_empty())
    assert is_pass == True, "fail the test"
    
    string_queue.enqueue("Hello")
    string_queue.enqueue("World")
    
    is_pass = (string_queue.size() == 2)
    assert is_pass == True, "fail the test"
    
    is_pass = (string_queue.peek() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test"
    
    is_pass = (string_queue.peek() == "Hello" and string_queue.size() == 2)
    assert is_pass == True, "fail the test"

    
    string_queue.enqueue("python")
    
    is_pass = (string_queue.is_full())
    assert is_pass == True, "fail the test" 
    
    try:
        string_queue.enqueue("rules")
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"
    
    string_queue.clear()
    
    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test" 
    
    try:
        string_queue.dequeue()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test" 
        
    try:
        string_queue.peek()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"
    
    int_queue = BoundedQueue(2000)
    for i in range(0, 1000):
        int_queue.enqueue(i)      
    correctOrder = True
    for i in range(0, 200):
        if int_queue.dequeue() != i:
            correctOrder = False
            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
    
    is_pass = (int_queue.size() == 800)
    assert is_pass == True, "fail the test" 
 
    is_pass = (int_queue.capacity() == 2000)
    assert is_pass == True, "fail the test"    

    is_pass = (int_queue.peek() == 200)
    assert is_pass == True, "fail the test"
    
    if is_pass == True:
        print ("=========== cong, your implementation passes the test ============")


#let's test it
if __name__ == '__main__':
    test()