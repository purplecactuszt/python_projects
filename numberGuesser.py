from random import randint
rndNum = int(input('Input a maximum random WHOLE number: '))

goal = randint(1,rndNum)

attempt = 0

while True:

    guess = int(input('Type a guess: '))

    if(guess > goal):
        print('To high! Guess lower!')
        attempt+=1
    elif(guess < goal):
        print('To low guess higher!')
        attempt+=1
    elif(guess == goal):
        attempt+=1
        print('U guessed the number! Well done! You have done it in: '+str(attempt)+' attempts!')
        break
