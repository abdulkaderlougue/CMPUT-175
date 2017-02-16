from bounded import BoundedQueue
def main():
    capacity = 3
    bq = BoundedQueue(capacity)
    while True:
        userInput = input('Add, Serve or Exit: ')
        if userInput == 'Exit':
            return False
        elif userInput == 'Add':
            try:
                name = input('Enter the name of the person to add: ')
                bq.enqueue(name)
                print('Add'+ name+ 'to the line')
            except Exception as e:
                print(e)
            finally:
                print('people in the line: ' + bq.__str__() + '\n')
        
        elif userInput == 'Serve':
            try:
                x = bq.dequeue()
                print(x+ ' has been served.')
            except Exception as e:
                print(e)
            finally:
                print('People in the line: ' + bq.__str__() + '\n')
main()