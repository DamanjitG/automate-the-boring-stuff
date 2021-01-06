# Takes in multiple text files and combines them into a spreadsheet named CombinedTextFiles.xlsx
# The CombinedTextFiles.xlsx present in the folder is the result of running this program on test1.txt and test2.txt

import os, openpyxl, sys

if len(sys.argv) > 1:
    wb = openpyxl.Workbook()
    sheet = wb.active
    files = sys.argv[1:]
    for textFileNum in range(len(files)):
        text = open(os.path.abspath(files[textFileNum]))
        lines = text.readlines()
        for lineNum in range(len(lines)):
            sheet.cell(row = lineNum + 1, column = textFileNum + 1).value = lines[lineNum] 
    
    wb.save('CombinedTextFiles.xlsx')

else: print("Please pass in the paths to the files which you wish to be converted into a spreadsheet.")