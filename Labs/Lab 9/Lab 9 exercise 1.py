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

file1 = open('hotels.data','r')
file2 = open('Restaurants.data','r')
webPage_H = open("index.html","w")
webPage_R = open("index.html","w")

title = '<html><body><h1>Query Results</h1>'
fromYYC = '<h2>From City: Calgary</h2><table>'
fromYEG = '<h2>From City: Edmonton</h2><table>'
fromYVR = '<h2>From City: Vancouver</h2><table>'
table1 = '<tr><td>Hotal</td><td>Reviews</td><td>Price per night</td><td>Detail</td></tr>'
table2 = '<tr><td>Hotal</td><td>Reviews</td><td>Price per night</td><td>Detail</td></tr>'
table3 = '<tr><td>Hotal</td><td>Reviews</td><td>Price per night</td><td>Detail</td></tr>'

userInput = input('please choose a web to view: ')
if userInput == '1':
    for line in file1:
        data = line.split(';')
        fileName = data[4].split(".")
        name = fileName[0] + ".html"
        if data[0] == 'YYC':
            ratings = Reviews(data[2])
            table1 += '<tr><td>'+data[1]+'</td><td>'+ratings+'</td><td>'+data[3]+'</td><td><a href="' + name + '">More...</a></td></tr>'
            eachPage = open(name,'w')
            eachPage.write(title+fromYYC+'<table><tr><td><img src="' + data[4] +'".jpg" /></td></tr><tr><td>' + data[6] +\
                                      '</td></tr></table>' + '<ul><li>Hotel: ' + data[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +'</li><li>Price per night: ' +\
                                      data[3] + '</li><li>URL: ' +'<a href="' + data[5] + '">' +data[5] + '</a></li><li>Phone: ' +\
                                      data[7] + '</li><li>Address: ' +data[8] + '</li></ul></body></html>')
            eachPage.close()
            
        if data[0]=='YEG':
            ratings = Reviews(data[2])
            table2 += '<tr><td>'+data[1]+'</td><td>'+ratings+'</td><td>'+data[3]+'</td><td><a href="' + name + '">More...</a></td></tr>'
            eachPage = open(name,'w')
            eachPage.write(title+fromYEG+'<table><tr><td><img src="' + data[4] +'".jpg" /></td></tr><tr><td>' + data[6] +\
                                      '</td></tr></table>' + '<ul><li>Hotel: ' + data[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +'</li><li>Price per night: ' +\
                                      data[3] + '</li><li>URL: ' +'<a href="' + data[5] + '">' +data[5] + '</a></li><li>Phone: ' +\
                                      data[7] + '</li><li>Address: ' +data[8] + '</li></ul></body></html>')
            eachPage.close()
            
    webPage_H.write(title+fromYYC+table1+'</table>'+fromYEG+table2+'/table'+'</body></html>')
    webPage_H.close()
        
if userInput == '2':
    for line in file2:
        data = line.split(';')
        fileName = data[4].split(".")
        name = fileName[0] + ".html"
        if data[0] == 'YYC':
            ratings = Reviews(data[2])
            table1 += '<tr><td>'+data[1]+'</td><td>'+ratings+'</td><td>'+data[3]+'</td><td><a href="' + name + '">More...</a></td></tr>'
            eachPage = open(name,'w')
            eachPage.write(title+fromYYC+'<table><tr><td><img src="' + data[4] +'".jpg" /></td></tr><tr><td>' + data[6] +\
                                      '</td></tr></table>' + '<ul><li>Hotel: ' + data[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +'</li><li>Price per night: ' +\
                                      data[3] + '</li><li>URL: ' +'<a href="' + data[5] + '">' +data[5] + '</a></li><li>Phone: ' +\
                                      data[7] + '</li><li>Address: ' +data[8] + '</li></ul></body></html>')
            eachPage.close()
            
        if data[0]=='YEG':
            ratings = Reviews(data[2])
            table2 += '<tr><td>'+data[1]+'</td><td>'+ratings+'</td><td>'+data[3]+'</td><td><a href="' + name + '">More...</a></td></tr>'
            eachPage = open(name,'w')
            eachPage.write(title+fromYEG+'<table><tr><td><img src="' + data[4] +'".jpg" /></td></tr><tr><td>' + data[6] +\
                                      '</td></tr></table>' + '<ul><li>Hotel: ' + data[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +'</li><li>Price per night: ' +\
                                      data[3] + '</li><li>URL: ' +'<a href="' + data[5] + '">' +data[5] + '</a></li><li>Phone: ' +\
                                      data[7] + '</li><li>Address: ' +data[8] + '</li></ul></body></html>')
            eachPage.close()        
        
        if data[0]=='YVR':
            ratings = Reviews(data[2])
            table2 += '<tr><td>'+data[1]+'</td><td>'+ratings+'</td><td>'+data[3]+'</td><td><a href="' + name + '">More...</a></td></tr>'
            eachPage = open(name,'w')
            eachPage.write(title+fromYEG+'<table><tr><td><img src="' + data[4] +'".jpg" /></td></tr><tr><td>' + data[6] +\
                                      '</td></tr></table>' + '<ul><li>Hotel: ' + data[1] + '</li><li>' +\
                                      'Reviews: ' + ratings +'</li><li>Price per night: ' +\
                                      data[3] + '</li><li>URL: ' +'<a href="' + data[5] + '">' +data[5] + '</a></li><li>Phone: ' +\
                                      data[7] + '</li><li>Address: ' +data[8] + '</li></ul></body></html>')
            eachPage.close()                    
            
        
            
    webPage_R.write(title+fromYYC+table1+'</table>'+fromYEG+table2+'/table'+fromYVR+table3+'</body></html>')    
    webPage_R.close()