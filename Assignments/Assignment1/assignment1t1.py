#This code is for assignmnet1 task1
import math
#open two files, file1 is calls.txt, file2 is customers.txt
file1 = open('calls.txt','r')
file2 = open('customers.txt','r')
###store two files in two list because file can only be read 1 time
file1List = []
file2List = []
for line in file1:
    file1List.append(line)
for line in file2:
    file2List.append(line)

#create five empty list called column 1-9 for print the format in the end
column1 = []  # Phone number
column2 = []  # Name
column3 = []  # #
column4 = []  # Duration
column5 = []  # Due

###code for column1 and column2 which are formatting the numbers and customers' name.###
#customers is a list which conatin all the info in the file.
#lines is each line in the file

customers = []  
unsortedPhoneNumber = []  #Empty list for unsorted phone number which will be used in column3 
for line in file2List:
    customers.append(line)
customers.sort()

for line in customers:
    lines = line.split(';')
    phoneNumber = lines[0]   #Phone Numbers which has been sorted
    unsortedPhoneNumber.append(phoneNumber)
    name = lines[1]         # customers names
    middleNumber = phoneNumber[3:6]  # three number in the middle of phone number
    lastNumber = phoneNumber[6:10]   # last 4 number
    prefix = '(780) '                # phone's prefix number
    sortedNumber = prefix + middleNumber + ' ' + lastNumber
    sortedName = name.ljust(30)
    column1.append(sortedNumber)
    column2.append(sortedName)


###code for column3 which is for the number of calls originating from the phone in question.###
caller = []                             #Empty list for the all the number of in call
for line in file1List:                  
    lines1 = line.split(';')            
    callerNumber = lines1[1]            #all the in call in the form of string
    caller.append(callerNumber)
for eachNumber in unsortedPhoneNumber:
    count = caller.count(eachNumber)    #times caller called
    column3.append(count)



###code for column4 which is total duration of the calls originating from the phone.###
for eachnumber in unsortedPhoneNumber:
    totalTime = 0                                       #set total time as 0
    balance = 0                                         #set balance as 0
    totalBalance = 0                                    #set total balance as 0
    for line in file1List:
        lines1 = line.split(';')
        if lines1[1] == eachnumber :
            totalTime += int(lines1[3])  
            #all the time in the form of second
            minute = math.ceil(int(lines1[3]) / 60)     #turn the seconds into minute
            balance = float(minute) * float(lines1[4])
            totalBalance += balance                     #balance been added
    print(totalTime)       
    m, s = divmod(totalTime, 60)
    h, m = divmod(m, 60)
    duration = "%dh%02dm%02ds" % (h, m, s)  #time period after been sorted
    column4.append(duration)
    column5.append(totalBalance)
    


###code for the total Dues
totalDues = 0                   # total Dues is for the total dues at line 16
for i in range(0,len(column5)):
    totalDues += column5[i]
    

###print the table
tableLine1 = '+--------------+------------------------------+---+---------+--------+'  #this is boarder of the table
tableLine2 = '| Phone number | Name                         | # |Duration | Due    |'  #this is content in the first line of the table
print(tableLine1)
print(tableLine2)
print(tableLine1)
for i in range(0,len(unsortedPhoneNumber)):
    
    table4_14 = '|'+column1[i]+'|'+column2[i]+'|'+str(column3[i])+'|'+column4[i]+'|$' + str('%7.2f' %(column5[i])) +'|'         #this code print the table line from 4 to 14
    
    if column5[i] > 850:
        print(table4_14 + '**')
    elif int(column3[i]) > 350:
        print(table4_14 + '++')
    else:
        print(table4_14)
print(tableLine1)
print('| Total dues   |' +'$'.rjust(43) + 
          '%10.2f' %(totalDues) + '|')
print(tableLine1)
        
        
        