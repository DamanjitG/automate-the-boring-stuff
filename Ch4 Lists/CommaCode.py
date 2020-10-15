def CommaCode(lst):
    outputString = ''
    for i in range(len(lst)):
        if i == len(lst) - 1:
            outputString = outputString + 'and ' + str(lst[i])
        else:    
            outputString = outputString + str(lst[i]) + ', '
    return outputString

# tests
print(CommaCode([1,2,3]))
print(CommaCode(['apples','bananas','tofu','cats']))
