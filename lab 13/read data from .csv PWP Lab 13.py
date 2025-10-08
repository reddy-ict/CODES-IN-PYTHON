import csv

file_path = r"C:\Users\reddy\Downloads\data-1(1).csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


