file = open('words.txt','r')
separater = [' ', ',', "'",'"', '.', ':']
wordString = []
word = ''
for line in file:
    for letter in line:
        if letter not in separater:
            string = letter.strip('\n')
            word += string
        else:
            wordString.append(word.strip('\n'))
            word = ''
    checkList = []
    for letter in wordString:
        if letter != '':
            checkList.append(letter.lower())
    wordList = []
    for letter in checkList:
        if letter not in wordList:
            wordList.append(letter)
    for item in wordList:
        count = (item + ': ' + str(checkList.count(item)))
        print(count.lower() + '\n')
            