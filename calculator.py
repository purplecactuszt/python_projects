while True:
    #gets all of the information for what and how to calculate
    a = float(input('\nWrite the first number: '))

    r = str(input('Write what do you want to do (+,-,/,*): '))

    b = float(input('Write the second number: '))

    #checks how to calculate

    if (r == '+'):
        result = a+b
        print(str(a)+' '+r+' '+str(b)+' = '+str(result))
    elif(r == '-'):
        result = a-b
        print(str(a)+' '+r+' '+str(b)+' = '+str(result))
    elif(r == '/'):
        result = a/b
        print(str(a)+' '+r+' '+str(b)+' = '+str(result))
    elif(r == '*'):
        result = a*b
        print(str(a)+' '+r+' '+str(b)+' = '+str(result))
    else:
        print('Invalid character!')
        pass
    #asks to continue
    rep = str(input('Do you want to restart?(y/n): '))
    if (rep == 'y'):
        #continue
        pass
    elif(rep == 'n'):
        #stop
        break
    else:
        break
