def collatz(num):
    number = int(num)
    if number % 2 == 0:
        newNumber = number//2
        print(newNumber)
        return(newNumber)
    elif (number + 1) % 2 == 0:
        newNumber = 3 * number + 1
        print(newNumber)
        return(newNumber)

correctInput = False
while correctInput == False:
    chosenNumber = input('Which number would you like to demonstrate the Collatz sequence with?')
    try:
        while chosenNumber != 1:
            chosenNumber = collatz(chosenNumber)
        correctInput = True
    except ValueError:
        print('Please enter an integer.')
        continue
    