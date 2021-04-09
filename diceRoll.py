from random import randint


while True:
    roll = randint(1,6)
    print('Dice roll is: '+str(roll))

    stop = str(input('Wana roll again?? If yes type r and hit enter if no just hit enter: '))

    if(stop == 'r'):
        pass
    else:
        break
