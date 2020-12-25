import re
exp = input("Please input a regex expression.")
userRegex = re.compile(exp)
file = open(input("Please input the path to the file you wish to search."))
fileContent = file.read()
file.close()
print("Here are all matches found:"+"\n")
for match in userRegex.findall(fileContent):
    print(match+"\n")