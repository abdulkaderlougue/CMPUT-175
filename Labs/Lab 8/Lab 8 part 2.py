print('User or Computer:Computer')
gameOver = False
low = 0
high = 100
guess = (low + high)//2
while not gameOver:
    print('Computer Guess: '+ str(guess))
    judge=input('')    
    if judge == 'win':
        print('Hooray the computer won')
        gameOver = True
    elif judge == 'exit':
        gameOver = True
    
    elif judge == '-':
        high = guess - 1
        guess = (low + high)//2
    elif judge == '+':
        low = guess + 1
        guess = (low + high)//2
        