import random
answer = random.randint(0,100)
chance = 6
gameOver = False
while not gameOver:
    while chance > 0:
        userAnswer = input('enter a number between 0 and 100: ')
        if userAnswer == str(answer):
            print('Hooray you won!')
            gameOver = True
            break
        elif userAnswer == 'exit':
            gameOver = True
            break
        else:
            chance -= 1
            if int(userAnswer) > answer:
                print('Too high')
            else:
                print('Too low')
                
    if chance == 0:
        print('Ohh no you lost, the correct number is '+answer)
        gameOver = True