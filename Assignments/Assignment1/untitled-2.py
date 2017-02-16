import os, sys

# Reads the two data files
try:
    file1 = open("customers.txt", "r")
    file2 = open("calls.txt", "r")
    stop = False
except FileNotFoundError:
    print("Error: File Not Found!")
    stop = True

if stop == False:
    # Create a new file called "callgraph.txt"
    newFile = open("callgraph.txt", "w")
    
    # Creates two lists:
    # One to store the customers,
    # another to store the numbers only.
    customerList = []
    numberList = []
    for line in file1:
        customerList.append(line)
        info = line.split(";")
        numberList.append(info[0])
    
    
    # Use a dictionary to assign an index to each phone number, 
    # then sort the dictionary by phone number to get a list of sorted index
    phoneNumberWithIndex = {}
    for index in range(0,len(numberList)):
        phoneNumberWithIndex[index + 1] = numberList[index]
    sortedIndex = sorted(phoneNumberWithIndex, key=lambda x:phoneNumberWithIndex[x])

    # Sort the customers by phone numbers
    customerList.sort()
    numberList.sort()
    print(numberList)
    # Creates an empty list callRecord[] to store the call record.
    callRecord = []
    for line in file2:
        count = line.split(";")
        callRecord.append(count)
        
    # timeCount[] is the list of total calling time of each customer
    timeCount = []
    for line1 in numberList:
        
        # Initialize the variable 'duration' that will be used later
        # to count the time
        duration = 0
    
        # When the calling number matches the phone number in question,
        # (the phone number will be questioned in order of existance in the list)
        # sum up the calling time  
        for line2 in callRecord:
            if line2[1] == line1:
                duration += int(line2[3])
        timeCount.append(duration)
        
    # Use a dictionary to assign the call time to each phone number, 
    # then sort the dictionary by phone number to get a list of sorted time
    phoneNumberWithTime = {}
    for index in range(0,len(numberList)):
        phoneNumberWithTime[timeCount[index]] = numberList[index]
    sortedTime = sorted(phoneNumberWithTime, key=lambda x:phoneNumberWithTime[x])
        
    # Converts the number values in the list from int to str,
    # in order to print it
    for index in range(0,len(sortedIndex)):
        sortedIndex[index] = str(sortedIndex[index])
    for index in range(0,len(sortedTime)):
        sortedTime[index] = str(sortedTime[index])
    
    # Create lists to store each customer's info:
    # nameList[] to store customer's name,
    # residencyList[] to store customer's location of residence
    nameList = []
    residencyList = []
    index = 0
    for line in customerList:
        data = line.replace("\n","")
        info = data.split(";")
        nameList.append(info[1])
        residencyList.append(info[2])
        index += 1
    # Choose how the graph is directed.
    # Repeats forever if the user enters anything other than "0" and "1".
    direct = 2
    while direct < 0 or direct > 1:
        try:
            direct = int(input("\n"
                               "\n"
                               "Data for:\n" 
                               "Directed graph .....1\n" 
                               "Undirected graph ...0\n"
                               "\n"
                               "User input: "))
        except ValueError:
            None
    
    # Choose the edge weight.
    # Repeats forever if the user enters anything other than "0" and "1".
    edgeWeight = None
    while edgeWeight < 0 or edgeWeight > 1:
        try:
            edgeWeight = int(input("\n"
                                   "\n"
                                   "Edge weight is:\n"
                                   "The number of calls ...1\n"
                                   "The time spent ........0\n"
                                   "\n"
                                   "User input: "))
        except ValueError:
            None
    
    # Print out the table
    for index in range(0,len(sortedIndex)):
        dataList = (sortedIndex[index] + ", " + numberList[index] + ", " + nameList[index] 
                    + ", " + residencyList[index] + ", " + sortedTime[index] + "\n")
        newFile.write(dataList)
        print(dataList)
    # Separate the table of customers and the call graph by an empty line
    newFile.write("\n")
    
    # If the graph is directed
    if direct == 1:
        for index1 in range(0,len(sortedIndex)):
            for index2 in range(0,len(sortedIndex)):
                try:
                    if sortedIndex[index1] != sortedIndex[index2]:
                        if edgeWeight == 1:
                            callCount = 0
                            for line in callRecord:
                                if numberList[index1] == line[1] and numberList[index2] == line[2]:
                                    callCount += 1
                            caller_receiver = sortedIndex[index1] + ", " + sortedIndex[index2] + ", " + str(callCount) + "\n"
                            newFile.write(caller_receiver)   
                        else:
                            duration = 0
                            for line in callRecord:
                                if numberList[index1] == line[1] and numberList[index2] == line[2]:
                                    duration += int(line[3])
                            caller_receiver = sortedIndex[index1] + ", " + sortedIndex[index2] + ", " + str(duration) + "\n"
                            newFile.write(caller_receiver)
                except IndexError:
                    None
                    
    # If the graph is undirected
    else:
        
        # Create lists call[] and receive[] to store the numbers already processed,
        # so we could prevent a pair(call = Albert, receive = Bob) of data being generated
        # if the pair(call = Bob, receive = Albert) already exist,
        # because this is a undirected graph, which means each pair is double-sided,
        # so it should be only called ONCE.
        call = []
        receive = []    
        
        for index1 in range(0,len(sortedIndex)):
            for index2 in range(1,len(sortedIndex)):
                try:              
                    if sortedIndex[index1] != sortedIndex[index2]:                   
                        if edgeWeight == 1:
                            callCount = 0
                            for line in callRecord:
                                if numberList[index1] == line[1] and numberList[index2] == line[2]\
                                or numberList[index1] == line[2] and numberList[index2] == line[1]:
                                    callCount += 1                       
                            caller_receiver = sortedIndex[index1] + ", " + sortedIndex[index2] + ", " + str(callCount) + "\n"
                            call.append(sortedIndex[index1])
                            receive.append(sortedIndex[index2])
                            checkExist = caller_receiver.split(", ")
                            if checkExist[1] in call:
                                if checkExist[0] not in receive:
                                    newFile.write(caller_receiver)
                            else:
                                newFile.write(caller_receiver)
                            
                        # If the user is asking for calling time
                        # from the number on the left to the number on the right                    
                        else:
                            duration = 0
                            for line in callRecord:
                                if numberList[index1] == line[1] and numberList[index2] == line[2]\
                                or numberList[index1] == line[2] and numberList[index2] == line[1]:
                                    duration += int(line[3])
                            caller_receiver = sortedIndex[index1] + ", " + sortedIndex[index2] + ", " + str(duration) + "\n"
                            call.append(sortedIndex[index1])
                            receive.append(sortedIndex[index2])
                            checkExist = caller_receiver.split(", ")
                            if checkExist[1] in call:
                                if checkExist[0] not in receive:
                                    newFile.write(caller_receiver)
                            else:
                                newFile.write(caller_receiver)                        
                except IndexError:
                    None

newFile.close()