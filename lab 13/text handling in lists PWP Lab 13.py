file1 = r"C:\Users\reddy\Documents\DR's Reddy.txt"

lines_list = []
with open(file1, "r") as file:
    for line in file:
        lines_list.append(line.strip())

print("List of lines:", lines_list)


