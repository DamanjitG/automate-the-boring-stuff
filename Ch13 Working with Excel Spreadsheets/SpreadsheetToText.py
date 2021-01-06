# This program performs the reverse of TextToSpreadsheet; that is, it takes a spreadsheet and converts it into a series of text files,
#   such that each text file consists of the cells in one column, where each row is a newline
# The files text1.txt and text2.txt in the folder are the result of running this program on CombinedTextFiles.xlsx

import os, openpyxl, sys

if len(sys.argv) == 2:
    wb = openpyxl.load_workbook(os.path.abspath(sys.argv[1]))
    sheet = wb.active
    for columnNum in range(len(list(sheet.columns))):
        text = open('text'+str(columnNum+1)+'.txt', 'a')
        i=0
        for cell in list(sheet.columns)[columnNum]:
            text.write(cell.value)

        text.close()

else: print("Please pass in only the path to the spreadsheet you wish to convert to text files.")

