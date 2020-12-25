import shutil, os
from pathlib import Path

extension = input("Please enter the file extension you would like to search for; for example, png, jpg, pdf\n")
folder = input("Please enter the absolute path to the folder you would like to search through.")
destination = input("Please enter the absolute path to the folder you would like to copy the files to. \n")

for foldername, subfolders, files in os.walk(folder):
    if foldername != destination: # takes care of the case where the destination is a subfolder of the folder being searched through
        for file in list(Path(foldername).glob('*.'+extension)):
            shutil.copy(file, destination)   