board = [[' ']*20 for row in range(10)]
print(board)
letterList = ['A', 'B','C','D','E','F','G','H','I','J']
index = 0
for line in board:
    leftIndex =  "%2d"%(letterList[index])
    row = '|'
    for grid in line:
        if index < 10:
            grid += '|'
            row += grid
            index += 1
        row+='\t'
        row+= "%2d"%(letterList[index-9])
        if index > 9:
            grid += '\t'
            row += grid
            index += 1
            