#python files
import os

file_path = "C:\\dev\\git-code\\python-praticing\\act3\\stuff\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else: 
    print("That location doesn't exist")

if os.path.isfile(file_path):
    print("That is a file")
elif os.path.isdir(file_path):
    print("that is a folder")
else:
    print("That location doesn't exists ")