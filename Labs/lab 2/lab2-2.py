#Write a number guessing game. The program will start by choosing a random number between 1 and 20 (inclusive). 
#The user has 6 chances to guess what the number is. The program should end when either the user guesses the correct number,
#or else they have no guesses left. A message should inform the user if they guessed correctly or ran out of guesses. When the 
#user enters a guess, the program must check that the guess is between 1 and 20 (inclusive).
import random
chance = 0
answer = random.randint(1,20)
while chance < 6:
    userAnswer = input('Enter a guess (1-20):')
    if answer < int(userAnswer) <= 20:
        print('Too high!')
        chance += 1
        if chance == 6:
            print('You are out of guesses. The number was' + str(answer) + '.')
            break
    elif 0 < int(userAnswer) < answer: 
        print('Too Low!')
        chance +=1
        if chance == 6:
            print('You are out of guesses. The number was' + str(answer) + '.')
            break
    elif int(userAnswer) > 20 or int(userAnswer) < 1:
        print('That number is not between 1 and 20!')
    elif int(userAnswer) == int(answer):
        print('Correct! The number was'+ str(answer) + '.')
        break
    