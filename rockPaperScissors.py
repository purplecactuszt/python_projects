from random import randint
gamesPlayed = 0
win = 0
tie = 0
lose = 0
while True:
    computer = randint(1,3)

    if (computer == 1):
        computerChose = 'rock'
    elif(computer == 2):
        computerChose = 'paper'
    else:
        computerChose = 'scissors'

    playerChose = str(input('Enter your pick (rock/paper/scissors): '))
    if(playerChose == 'rock' and computerChose == 'rock'):
        print("It's a tie, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        tie+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'rock' and computerChose == 'paper'):
        print("It's a loss, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        lose+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'rock' and computerChose == 'scissors'):
        print("It's a win, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        win+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'paper' and computerChose == 'rock'):
        print("It's a win, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        win+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'paper' and computerChose == 'paper'):
        print("It's a tie, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        tie+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'paper' and computerChose == 'scissors'):
        print("It's a loss, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        lose+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'scissors' and computerChose == 'rock'):
        print("It's a loss, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        lose+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'scissors' and computerChose == 'paper'):
        print("It's a win, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        win+=1
        pass
        gamesPlayed+=1
    elif(playerChose == 'scissors' and computerChose == 'scissors'):
        print("It's a tie, computer chose: "+computerChose+' and you chose: '+playerChose+'.')
        tie+=1
        pass
        gamesPlayed+=1
    print('You have played: '+str(gamesPlayed)+' games.')
    print('You have won: '+str(win)+' games.')
    print('You have lost: '+str(lose)+' games.')
    print('You have ties: '+str(tie)+' games.')
    continues = str(input('Wana continue? (y/n): '))

    if(continues == 'y'):
        pass
    else:
        break
