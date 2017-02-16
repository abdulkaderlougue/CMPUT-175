#from Lab_6_exercise1 import CircularQueue
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
        if  type(self.__capacity) != int or self.__capacity<=0:
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
        self.__items
    
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
    normal = CircularQueue(3)
    vip = CircularQueue(3)
    commandList = ['add','serve','exit']
    while True:
        command = input('Add, Serve, or Exit: ')
        if command == 'exit':
            return False      
        elif command == 'serve' or command == 'Serve':
            
            if vip.isEmpty():
                try:
                    a = normal.peek()
                    x = normal.dequeue(a)
                    print (a + 'has been served')
                except Exception:
                    print('normal queue is empty')
                finally:
                    print('People in the line: ' + normal.__str__() + "\n")
                    print('VIP customers queue:' + vip.__str__() + '\n')                
            
            else:
                try:
                    b = vip.peek()
                    y = vip.dequeue(b)
                    print (b + 'has been served')
                except Exception:
                    print('vip queue is empty')
                    
                finally:
                    print('People in the line: ' + normal.__str__() + "\n")
                    print('VIP customers queue:' + vip.__str__() + '\n')
                
                
        elif command == 'add' or command == 'Add':
            try:
                name = input('Enter the name of the person to add: ')
                checkVip = input('Is the customer VIP?')
                customer = name + " "
                if checkVip == 'yes':
                    #if customer not in vip.elements:
                    if vip.size() < 3:
                        vip.enqueue(customer + " ")
                        print ('Add '+ customer + 'to the line.')
                    else:
                        print ('Error: VIP customer queue is full')
                        #print (customer + 'is already in line.')
                else:
                    if normal.size() < 3:
                        normal.enqueue(customer + " ")
                        print (customer + 'is already in line.')
                    else:
                        print ('Error: Normal customer queue is full')
                        
            except Exception as e:
                print (e)
            finally:
                print ('People in the line: ' + normal.__str__() + "\n")
                print('VIP customers queue:' + vip.__str__() + '\n')
        
        
        else:
            print('Invalid command! \n')
            
           
                       
main()    
    