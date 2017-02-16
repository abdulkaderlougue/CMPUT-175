import math

def Reviews(score):
    full = math.floor(float(score))
    empty = 5 - math.ceil(float(score))
    half = 5 - full - empty
    rating = '<img src="star-full.png" style="width:20px;height:20px">' * full +\
        '<img src="star-half.png" style="width:20px;height:20px">' * half +\
        '<img src="star-empty.png" style="width:20px;height:20px">' * empty
    rating_with_score = rating + '(' + score + ')'
    return rating_with_score
    
for index in range(2):
    if index == 0:
        file = open("hotels.data","r")
        webpage = open("hotels.html","w")
    else:
        file = open("restaurants.data","r")
        webpage = open("restaurants.html","w")        
    dataList = []
    categoryLine = True
    for line in file:
        newLine = line.replace("\n","")
        data = newLine.split(";")    
        if categoryLine == True:
            category = data[1]
            costTitle = data[3]
            categoryLine = False
        else:
            if "$" in data[3]:
                intCost = data[3].strip("$")
                data[3] = int(intCost)
            dataList.append(data)
    
    # Selection Sort according to cost
    for index in range(len(dataList)):
        smallIndex = index
        for i in range(index, len(dataList)): # finding smallest
            if dataList[i][3] < dataList[smallIndex][3]:
                smallIndex = i
                
        temp = dataList[index] # swapping
        dataList[index] = dataList[smallIndex]
        dataList[smallIndex] = temp
    
    Calgary,Edmonton,Vancouver = [],[],[]      
    for item in dataList:
        item[3] = "$" + str(item[3])
        if item[0] == "YYC":
            Calgary.append(item)
        elif item[0] == "YEG":
            Edmonton.append(item)
        elif item[0] == "YVR":
            Vancouver.append(item)
    
    title = "<!DOCTYPE html><html><body><h1>Query Results</h1>"
    calgaryTitle,calgaryTable,calgaryFooter = "","",""
    edmontonTitle,edmontonTable,edmontonFooter = "","",""
    vancouverTitle,vancouverTable,vancouverFooter = "","",""
    
    if len(Calgary) > 0:
        calgaryList = []
        index = 0
        calgaryTitle = "<h2>From City: Calgary</h2><table><tr><th>" + category +\
            "</th>" +"<th>Reviews</th><th>" + costTitle +\
            "</th><th>Details</th></tr>"
        calgaryTable = ""
        
        for item in Calgary:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"
            calgaryList.append(name)
        calgaryFiles = [open(path, 'w') for path in calgaryList]
        
        for item in Calgary:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"
            
            ratings = Reviews(item[2])
            calgaryTable += '<tr><td>' + item[1] + '</td><td>' + ratings +\
                '</td><td>' + item[3] +\
                '</td><td><a href="' + name + '">More...</a></td></tr>'
            
            item[5] = "http://" + item[5]
            calgaryFiles[index].write(title + '<h2>From City: Calgary</h2>' +\
                                      '<table><tr><td><img src="' + item[4] +\
                                      '".jpg" /></td></tr><tr><td>' + item[6] +\
                                      '</td></tr></table>' + '<ul><li>' +\
                                      category + ': ' + item[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +\
                                      '</li><li>' + costTitle + ': ' +\
                                      item[3] + '</li><li>URL: ' +\
                                      '<a href="' + item[5] + '">' +\
                                      item[5] + '</a></li><li>Phone: ' +\
                                      item[7] + '</li><li>Address: ' +\
                                      item[8] + '</li></ul></body></html>')
            calgaryFiles[index].close()
            index += 1
        calgaryFooter = "</table>"
            
    if len(Edmonton) > 0:
        edmontonList = []
        index = 0
        edmontonTitle = "<h2>From City: Edmonton</h2><table><tr><th>" + category +\
            "</th>" +"<th>Reviews</th><th>" + costTitle +\
            "</th><th>Details</th></tr>"
        edmontonTable = ""
        
        for item in Edmonton:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"
            edmontonList.append(name)
        edmontonFiles = [open(path, 'w') for path in edmontonList]    
        
        for item in Edmonton:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"        
    
            ratings = Reviews(item[2])
            edmontonTable += '<tr><td>' + item[1] + '</td><td>' + ratings +\
                '</td><td>' + item[3] +\
                '</td><td><a href="' + name + '">More...</a></td></tr>'
            
            item[5] = "http://" + item[5]
            edmontonFiles[index].write(title + '<h2>From City: Edmonton</h2>' +\
                                       '<table><tr><td><img src="' + item[4] +\
                                       '".jpg" /></td></tr><tr><td>' + item[6] +\
                                       '</td></tr></table>' + '<ul><li>' +\
                                       category + ': ' + item[1] + '</li><li>' +\
                                       'Reviews: ' + ratings +\
                                       '</li><li>' + costTitle + ': ' +\
                                       item[3] + '</li><li>URL: ' +\
                                       '<a href="' + item[5] + '">' +\
                                       item[5] + '</a></li><li>Phone: ' +\
                                       item[7] + '</li><li>Address: ' +\
                                       item[8] + '</li></ul></body></html>')
            edmontonFiles[index].close()
            index += 1
        edmontonFooter = "</table>"
            
    if len(Vancouver) > 0:
        vancouverList = []
        index = 0
        vancouverTitle = "<h2>From City: Vancouver</h2><table><tr><th>" +\
            category + "</th>" +"<th>Reviews</th><th>" + costTitle +\
            "</th><th>Details</th></tr>"
        vancouverTable = ""
        
        for item in Vancouver:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"
            vancouverList.append(name)
        vancouverFiles = [open(path, 'w') for path in vancouverList]
        
        for item in Vancouver:
            fileName = item[4].split(".")
            name = fileName[0] + ".html"
            
            ratings = Reviews(item[2])
            vancouverTable += '<tr><td>' + item[1] + '</td><td>' + ratings +\
                '</td><td>' + item[3] +\
                '</td><td><a href="' + name + '">More...</a></td></tr>'
            
            item[5] = "http://" + item[5]
            vancouverFiles[index].write(title + '<h2>From City: Vancouver</h2>' +\
                                        '<table><tr><td><img src="' + item[4] +\
                                        '".jpg" /></td></tr><tr><td>' + item[6] +\
                                        '</td></tr></table>' + '<ul><li>' +\
                                        category + ': ' + item[1] + '</li><li>' +\
                                        'Reviews: ' + ratings +\
                                        '</li><li>' + costTitle + ': ' +\
                                        item[3] + '</li><li>URL: ' +\
                                        '<a href="' + item[5] + '">' +\
                                        item[5] + '</a></li><li>Phone: ' +\
                                        item[7] + '</li><li>Address: ' +\
                                        item[8] + '</li></ul></body></html>')
            vancouverFiles[index].close()
            index += 1
        vancouverFooter = "</table>"
    
    title = "<!DOCTYPE html><html><head><style>" +\
        "table, th, td{border: 1px solid black}" +\
        "table{border-spacing: 2px}</style></head><body><h1>Query Results</h1>"
    webpage.write(title + calgaryTitle + calgaryTable + calgaryFooter +\
                  edmontonTitle + edmontonTable + edmontonFooter +\
                  vancouverTitle + vancouverTable + vancouverFooter +\
                  "</body></html>")
    webpage.close()