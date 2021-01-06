import os, sys, openpyxl

if len(sys.argv) == 2:
    target = os.path.abspath(sys.argv[1])
    inputWb = openpyxl.load_workbook(target)
    inputSheet = inputWb.active
    outputWb = openpyxl.Workbook()
    outputSheet = outputWb.active
    for rowNum in range(1, len(list(inputSheet.rows)) + 2):
        for colNum in range(1, len(list(inputSheet.columns)) + 2):
            outputSheet.cell(row = rowNum, column = colNum).value = inputSheet.cell(row = colNum, column = rowNum).value

    outputWb.save(target)

else: print("Please pass only one input; the path to the excel spreadsheet you wish to invert.")