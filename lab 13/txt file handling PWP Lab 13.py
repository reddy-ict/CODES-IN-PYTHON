file1 = open(r"C:\Users\reddy\Documents\DR's Reddy.txt")
for each in file1:
    print(each)
    
with open(r"C:\Users\reddy\Documents\DR's Reddy.txt", "r") as file1:
    text = file1.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)

