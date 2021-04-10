import time
import os
start = input("Would you like to begin Timing? (y/n): ")
if start == "y":
    timeLoop = True
os.system('cls')

Sec = 0
Min = 0
Hour = 0

timeLoop = start
while timeLoop:
    Sec += 1
    print(str(Hour)+ ' Hours '+ str(Min) + " Mins " + str(Sec) + " Sec ")
    time.sleep(1)
    os.system('cls')
    if Sec == 60:
        Sec = 0
        Min += 1
    if Min == 60:
        Min = 0
        Hour += 1
