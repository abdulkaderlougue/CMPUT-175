userInput= input('Enter a string you want to reverse')
string = list(userInput)
theStack = []
for item in string:
    theStack.insert(0,item)
a=''.join(theStack)
print('The reversed String is: ' + a)