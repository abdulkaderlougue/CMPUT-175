class d_linked_node:
    
    def __init__(self, initData, initNext, initPrevious):
        # constructs a new node and initializes it to contain 
        # the given object (initData) and links to the given next 
        # and previous nodes. 
        self.__data = initData
        self.__next = initNext
        self.__previous = initPrevious
        if (initPrevious != None):
            initPrevious.__next = self
        if (initNext != None):
            initNext.__previous = self
    
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def getPrevious(self):
        return self.__previous
    
    def setData(self, newData):
        self.__data = newData
    
    def setNext(self, newNext):
        self.__next= newNext
    
    def setPrevious(self, newPrevious):
        self.__previous= newPrevious    

class d_linked_list:
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

            
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        temp = d_linked_node(item , None, None)
        if self.__head == None:
            self.__head = temp
            self.__tail = temp
        else:
            self.__head.setPrevious(temp)
            temp.setNext(self.__head)
            self.__head = temp
        
    def remove(self, item):
        # TODO:
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                preivous = current
                current = current.getNext()
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.__tail = previous
        self.__size -= 1
        
        
    def append(self, item):
        # TODO:
        temp = d_linked_node(item,None,None)
        if (self.__head == None):
            self.__head = temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.tail)
            
        self.__tail = temp
        self.__size += 1
        
    def insert(self, pos, item):
        # TODO:
        count = 0
        current = self.__head
        temp = d_linked_node(item,None,None)
        while current != None:
            if count  == pos:
                after = current.getNext()
                current.setNext(temp)
                temp.setPrevious(current)
                temp.setNext(after)
                after.setPrevious(temp)
                self.__size += 1
            else:
                count += 1
                current = current.getNext()
            
        
    def pop1(self):
        # TODO:
        if (self.__head == None):
            raise ('list is empty')
        else:
            self.__tail = self.__tail.getPrevious()
            
            
    def pop(self, pos):
        # TODO:
        count = 0
        current = self.__head
        while current != None:
            if count == pos:
                previous = current.getPrevious()
                theNext = current.getNext()
                previous.setNext(theNext)
                theNext.setPrevious
            else:
                count += 1
                current = current.getNext()
                
    def search_larger(self, item):
        # TODO:
        pos = 0
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData > item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found == False:
            pos = -1
            
        return pos
    
        
    def get_size(self):
        # TODO:    
        return self.__size
    
    def get_item(self, pos):
        # TODO:   
        current = self.__head
        count = 0
        while current != None:
            if count == pos:
                current.getData()
            else:
                current = current.getNext()
                count += 1
        
    def __str__(self):
        # TODO:   
        s = '['
        i = 0
        current = self.__head
        while current != None:
            if i >0:
                s = s+ ','
            dataObject = current.getData()
            if dataObject != None:
                s = s + '%s'%dataObject
                i = i+1
            current= current.getNext()
            
        s=s+']'
        return s
                
        

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop1() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()