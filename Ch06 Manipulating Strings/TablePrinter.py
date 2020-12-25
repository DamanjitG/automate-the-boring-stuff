def maxLength(strings):
    max = 0
    for string in strings:
        if len(string) > max:
            max = len(string)
    return max

def printTable(tableData):
    colWidth = [0] * len(tableData)
    for i in range(len(colWidth)):
        colWidth[i] = maxLength(tableData[i])
    for word in range(len(tableData[0])):
        for list in range(len(tableData)): 
            print(tableData[list][word].rjust(colWidth[list]), end=' ')
        print()
     
testData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(testData)