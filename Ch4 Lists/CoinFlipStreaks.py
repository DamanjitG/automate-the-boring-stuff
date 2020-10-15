import random
numberOfStreaks = 0 
for experimentNumber in range(10000):
    coinFlips = []
    for i in range(100):
        coinFlips.append(random.randint(0,1))
    
    streakPresent = False
    for i in range(94):
        if not streakPresent:
            if coinFlips[i] == coinFlips[i+1]:
                if coinFlips[i+1] == coinFlips[i+2]:
                    if coinFlips[i+2] == coinFlips[i+3]:
                        if coinFlips[i+3] == coinFlips[i+4]:
                            if coinFlips[i+4] == coinFlips[i+5]:
                                streakPresent = True
    if streakPresent:
        numberOfStreaks += 1
                            

print('Chance of streak: %s%%'% (numberOfStreaks/100))


