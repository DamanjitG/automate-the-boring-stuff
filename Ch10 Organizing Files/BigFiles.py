import os
from pathlib import Path

target = input("Please enter the absolute path of the folder you would like to search through.\n")
print("The following files are larger than 100 megabytes.")
for folder, subfolders, files in os.walk(target):
    for file in files:
        if os.path.getsize(os.path.join(folder, file)) / 1000000 > 100: #converting from bytes to megabytes, then checking if more than 100 mb
            print(os.path.join(folder, file))