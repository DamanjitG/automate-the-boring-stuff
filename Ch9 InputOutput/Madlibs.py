targetFile = input("Please type the path of the file that you would like to use as your template.\n")
template = open(targetFile)
templateContent = template.read()
template.close()
words = templateContent.split()
for i in range(len(words)):
    if words[i] in ("NOUN", "ADJECTIVE", "VERB", "ADVERB"):
        words[i] = (input("Please input a "+words[i].lower()+".\n")+" ")
    elif words[i][:-1] in ("NOUN", "ADJECTIVE", "VERB", "ADVERB"):
        words[i] = (input("Please input a "+words[i].lower()+"\n")+words[i][-1]+" ")
    elif i != (len(words) - 1):
        words[i] = (words[i]+" ")

newContent = ''.join(words)
newFile = open('madlib.txt', 'w')
newFile.write(newContent)
newFile.close()
print("Your madlib has been written to a file. Here are the contents:")
madlib = open('madlib.txt')
print(madlib.read())
madlib.close()