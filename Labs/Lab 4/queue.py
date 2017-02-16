# CMPUT 175 Winter 2013 Lab 4 Exercise 1
# This file implements the Queue class and can be used to test the Queue.


    
# Main function, which can be used to test your queue implementation:
def main():
    string_queue = Queue()
    int_queue = Queue()
    print("Initial size of empty Queue is zero:", int_queue.size() == 0)
    print("is_empty() works correctly:", int_queue.is_empty())
    
    string_queue.queue("Hello")
    string_queue.queue("World")
    print("Queue size updates after adding items:", string_queue.size() == 2)
    print("Queue keeps correct ordering:", string_queue.peek() == "Hello")
    print("peek() does not change Queue:", string_queue.peek() == "Hello" 
          and string_queue.size() == 2)
    print("String representation of queue:", string_queue)
    
    string_queue.clear()
    print("peek() returns nothing when Queue is empty:", 
          string_queue.peek() == None)
    print("clear() sets size to 0:", string_queue.size() == 0)
    print("dequeue() returns nothing when Queue is empty:", 
          string_queue.dequeue() == None)
    
    for i in range(0, 1000):
        int_queue.queue(i)      
    correctOrder = True
    for i in range(0, 200):
        if int_queue.dequeue() != i:
            correctOrder = False
    print("Queue keeps correct ordering using dequeue():", correctOrder)
    print("Queue size updates after removing items:", int_queue.size() == 800)
    print("peek() works correctly after dequeue():", int_queue.peek() == 200)    

main()