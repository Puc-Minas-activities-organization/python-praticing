import json
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        print(f"csv file '{file_path}' was created")
        writer.writerows(employees)
        
except FileExistsError:
    print(f"csv file {file_path} already exists")