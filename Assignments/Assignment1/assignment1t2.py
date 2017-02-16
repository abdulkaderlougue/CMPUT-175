###open two file
file1 = open('customers.txt','r')
file2 = open('calls.txt','r')
newFile = open("callgraph.txt", "w")
### create two list to store the two files
file1List = []
file2List = []
for line in file1:
    file1List.append(line)
for line in file2:
    file2List.append(line)  

### info for the table1
numberOfOrgin = {} #empty dictionary for storing number of origin as key, phone number as value
customers = []  # empty list for storing eachline which have been added number
table1Line = [] # empty list for storing the whole table1
callers = []    # empty list for storing numbers
phoneList =[]   #empty list for storing 9 numbers
number = 1      # the number before phone number
for line in file1List:
    line += ';'+ str(number)
    number +=1
    replace1 = line.replace("\n","")    #variable for delete \n and \r
    replace2 = replace1.replace("\r","")   #same 
    customers.append(replace2)
customers.sort()
for info in customers:
    totalTime = 0                       # for total time caller calls
    customersInfo = info.split(';')     #a list for all infomation of customers which contains number
    callers.append(customersInfo[3])
    phoneList.append(customersInfo[0])
    for line2 in file2List:
        lines2 = line2.split(';')       #each line in file2list 
        if lines2[1] == customersInfo[0]:
            totalTime += int(lines2[3]) 
    customersInfo.append(str(totalTime))
    numberOfOrgin[customersInfo[3]] = customersInfo[0]   #expend the dictionary which has been created
    
    table1 = customersInfo[3]+', '+customersInfo[0]+', '+customersInfo[1]+', '+ customersInfo[2]+', '+customersInfo[4]+'\n' #each line in table1Line    
    table1Line.append(table1)

###write table into new file    
for eachLine in table1Line:
    newFile.write(str(eachLine))
newFile.write('\n'
              '\n')

###loop for call graph
# to choose the direct.
# Repeats forever if the user enters anything other than "0" and "1".
direct = None    #set direct as a none value
while direct < 0 or direct > 1:
    try:
        direct = int(input('Data for:\n' 
                           'Directed graph .....1\n' 
                           'Undirected graph ...0\n'
                           'Choose a number only either 1 or 0: ')) #user's input
    except ValueError:
        None

# to choose the edge weight.
# Repeats forever if the user enters anything other than "0" and "1".
edgeWeight = None  #set edgeWeight as none value
while edgeWeight < 0 or edgeWeight > 1:
    try:
        edgeWeight = int(input('Edge weight is:\n'
                               'The number of calls ...1\n'
                               'The time spent ........0\n'
                               'Choose a number only either 1 or 0: '))
    except ValueError:
        None


###code for Directed graph


table2line = []   #empty list for storing the whole table2 
if direct == 1:
    for i in range (0,len(callers)):       #two indexs in range 0,9
        for i2 in range (0,len(callers)):
            if numberOfOrgin[callers[i]] != numberOfOrgin[callers[i2]]:
                if edgeWeight == 1:
                    times = 0              #set time as 0 at begining
                    for line in file2List:
                        lines3 = line.split(';')   #each line in file2List
                        if phoneList[i] == lines3[1] and phoneList[i2] ==lines3[2]:
                            times = times + 1
                    table2 = callers[i]+ ', '+ callers[i2]+', '+str(times) + '\n'   #each line in table2
                    table2line.append(table2)
                if edgeWeight == 0:
                    duration = 0           #set duration as 0 at begining
                    for line in file2List:
                        lines4 = line.split(';')  #each line in file2list
                        if phoneList[i] == lines4[1] and phoneList[i2] ==lines4[2]:  
                            duration = duration + int(lines4[3])
                    table2 = callers[i]+ ', '+ callers[i2]+', '+str(duration) + '\n' #each line in table2
                    table2line.append(table2)
    ###write table 2
    for eachline in table2line:
        newFile.write(str(eachline))

newFile.close()
