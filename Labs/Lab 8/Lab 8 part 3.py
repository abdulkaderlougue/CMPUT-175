file = open("input.txt","r")
webpage = open("index.htm","w")
minimum = 101
maximum = 0
markSum = 0
people = 0
markList = [[],[],[],[],[],[],[],[],[],[]]
for line in file:
    data = line.split(' ')
    mark = int(data[1])
    
    if mark > maximum:
        maximum = mark
    if mark < minimum:
        minimum = mark
    markSum += mark
    people += 1
    
    if mark < 10:
        markList[0].append(mark)
    elif mark < 20:
        markList[1].append(mark)
    elif mark < 30:
        markList[2].append(mark)
    elif mark < 40:
        markList[3].append(mark)
    elif mark < 50:
        markList[4].append(mark)
    elif mark < 60:
        markList[5].append(mark)
    elif mark < 70:
        markList[6].append(mark)
    elif mark < 80:
        markList[7].append(mark)
    elif mark < 90:
        markList[8].append(mark)
    else:
        markList[9].append(mark)  
        
average = markSum / people

heading = '<html><body><h1>Welcome to statistics page!</h1>>'
summary = "<p>Average is: " + str(average) + "<br />" +\
          "Minimum is: " + str(minimum) + "<br />" +\
          "Maximum is: " + str(maximum) + '</p><table><tr>'


text = ''
for index in range(len(markList)):
    text += '<td valign="bottom"><div style="padding:20px;width:10px;height:' + str(len(markList[index])) + 'px;background:blue;border:1px solid red;"></div></td>'
    
bottom = '</tr><tr><td>[0-9]</td><td>[10-19]</td><td>[20-29]</td><td>[30-39]</td><td>[40-49]</td>' +\
        '<td>[50-59]</td><td>[60-69]</td><td>[70-79]</td><td>[80-89]</td><td>[90-99]</td>'

end = '</tr></table></body></html>'

webpage.write(heading + summary + text + bottom + end)
webpage.close()
