import sys, openpyxl, os

if len(sys.argv) == 4:
    start = int(sys.argv[1])
    amount = int(sys.argv[2])
    target = os.path.abspath(sys.argv[3])
    wb = openpyxl.load_workbook(target)
    sheet = wb.active
    sheet.insert_rows(start, amount)
    wb.save(target)

else: print("Please pass 3 inputs to the program; the row that you wish to start at, the amount of blank rows you would like to insert, and the path to the target excel spreadsheet.")