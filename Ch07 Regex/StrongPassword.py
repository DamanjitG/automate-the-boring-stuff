import re 

lowerCase = re.compile(r'[a-z]')
upperCase = re.compile(r'[A-Z]') 
numbers = re.compile(r'\d')
longPassword = re.compile(r'........') 

def passwordStrength(password):
    if None not in (lowerCase.search(password), upperCase.search(password), numbers.search(password), longPassword.search(password)):
        print("This password is strong.")
          
    else: 
        print("This password is not strong.")
        


