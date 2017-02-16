# CMPUT 175 Winter 2013 Lab 4 Exercise 1
# This file implements the Queue class and can be used to test the Queue.

class Queue:
    def __init__(self):
        self.items=[]
    def queue(self, item):
        return self.items.insert(0,item)
    
    def dequeue(self):
        if Queue.is_empty(self):
            return None        
        else:
            return self.items.pop()
             
 
    def peek(self):
        if Queue.is_empty(self):
            return None
        else:
            return self.items[len(self.items)-1]        

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        return repr(self.items)

def main():
    string_queue = Queue()
    int_queue = Queue()
    
    theEnd = False
    while theEnd == False:
        
            userInput = input('Add,Serve,or Exit: ')
            if userInput == 'Serve':
                if int_queue.is_empty():
                    print('The lineup is already empty')
                else:
                    print(string_queue.peek() + 'has been served')
                    string_queue.dequeue()
            
            if int_queue.size() == 3:
                print('You cannot add more people, the lineup is full!')
            else:
                if userInput == 'Add':
                    addName = input('Enter the name of the person to add: ')
                    string_queue.queue(addName)
                    print(string_queue)
                    print(int_queue.size())
            if userInput == 'Exit':
                theEnd = True
        
            
main()