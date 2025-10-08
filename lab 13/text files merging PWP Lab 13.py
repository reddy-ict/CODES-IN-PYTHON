file1_path = r"C:\Users\reddy\Documents\DR's Reddy.txt"
file2_path = r"C:\Users\reddy\Documents\marwadi.txt"
merged_path = r"C:\Users\reddy\Documents\merged.txt"

with open(file1_path, "r") as f1, open(file2_path, "r") as f2, open(merged_path, "w") as fout:
    fout.write(f1.read())
    fout.write("\n")
    fout.write(f2.read())

print("Files merged successfully into merged.txt")

