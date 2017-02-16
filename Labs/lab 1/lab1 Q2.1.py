import urllib.request
dictionary = {}
url = 'https://www.cs.ualberta.ca/'
page = urllib.request.urlopen(url)
pagetext = page.read().decode()
start = 0
while start != -1:
    start = pagetext.find('<a herf="')
    if start != -1:
        pagetext = pagetext[start+9:]
        a = pagetext.find('"')
        b = pagetext.find('>')
        c = pagetext.find('</a')
        aStr = pagetext[b+1:c]
        if aStr.find('<') == -1 and aStr.find('>')== -1:
            link = pagetext[:a]
            text = pagetext[b+1:c]
            dictionary[text]=link
print(dictionary)