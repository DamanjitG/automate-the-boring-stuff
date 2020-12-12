import re

def validDate(date): 
    thirtyDayMonths = ["04", "06", "09", "11"]  
    thirtyOneDayMonths = ["01", "03", "05", "07", "08", "10", "12"]
    dateFormatRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    mo = dateFormatRegex.search(date)
    day, month, year = mo.groups()
    day = int(day)
    year = int(year)
    if day > 0:
        if year <= 2999 and year >= 1000:
            if month in thirtyDayMonths and day <= 30:
                return True

            elif month in thirtyOneDayMonths and day <= 31:
                return True
            
            elif year % 4 == 0 and day <= 29:
                return True

            elif day <= 28:
                return True

            else: return False
        else: return False
    else: return False
