#print('\n' * 30)
from random import randint
import random
import string

wordChoser = randint(1,10)

numOfGuesses = 0

if(wordChoser == 1):
    word = 'gambit'
elif(wordChoser == 2):
    word = 'man'
elif(wordChoser == 3):
    word = 'women'
elif(wordChoser == 4):
    word = 'tractor'
elif(wordChoser == 5):
    word = 'barber'
elif(wordChoser == 6):
    word = 'cube'
elif(wordChoser == 7):
    word = 'dog'
elif(wordChoser == 8):
    word = 'cat'
elif(wordChoser == 9):
    word = 'fish'
else:
    word = 'monkE'
while True:
    guess = str(input('Type a guess: '))
    if (guess == word):
        print('U win')
        break
    else:
        hint = random.choice(word)
        print('one of the letters is: '+hint)
        numOfGuesses+=1
        if(numOfGuesses > 6):
            print('The word was: '+word+' you lose!!!')
            break
        else:
            pass
