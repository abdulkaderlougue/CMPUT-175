file = open("input.txt","r")
webpage = open("index.htm","w")

minimum,maximum,people,mark_sum,average = 100,0,0,0,0
mark_list = [[] for i in range(10)]
for line in file:
    if line != "":
        data = line.split(" ")
        mark = int(data[1])
        
        if mark < minimum:
            minimum = mark
        if mark > maximum:
            maximum = mark
        mark_sum += mark
        people += 1
        
        if mark < 10:
            mark_list[0].append(mark)
        elif mark < 20:
            mark_list[1].append(mark)
        elif mark < 30:
            mark_list[2].append(mark)
        elif mark < 40:
            mark_list[3].append(mark)
        elif mark < 50:
            mark_list[4].append(mark)
        elif mark < 60:
            mark_list[5].append(mark)
        elif mark < 70:
            mark_list[6].append(mark)
        elif mark < 80:
            mark_list[7].append(mark)
        elif mark < 90:
            mark_list[8].append(mark)
        else:
            mark_list[9].append(mark)

average = mark_sum / people
count_list = [None] * 10
for index in range(len(count_list)):
    count_list[index] = len(mark_list[index])

start = "<html><body><h1>Welcome to statistics page!</h1>"
summary = "<p>Average is: " + str(average) + "<br />" +\
          "Minimum is: " + str(minimum) + "<br />" +\
          "Maximum is: " + str(maximum) + '</p><table><tr>'

text = ''
for index in range(len(mark_list)):
    text += '<td valign="bottom"><div style="padding:20px;width:10px;height:' + str(count_list[index] * 15) + 'px;background:blue;border:1px solid red;"></div></td>'

text += '</tr><tr><td>[0-9]</td><td>[10-19]</td><td>[20-29]</td><td>[30-39]</td><td>[40-49]</td>' +\
        '<td>[50-59]</td><td>[60-69]</td><td>[70-79]</td><td>[80-89]</td><td>[90-99]</td>'

end = "</tr></table></body></html>"
    
webpage.write(start + summary + text + end)
webpage.close()