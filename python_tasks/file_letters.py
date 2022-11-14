# Ques: To count the number of letters present in a text file

Data = open("newfile.txt", "w")
Data.write("Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is "
           "Open.")
Data.close()

a = "n"
count = 0

with open("newfile.txt", "r") as f:
    Data = f.read()
    for i in Data:
      if i == a:
        count = count + 1

print(count)
