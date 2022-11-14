# Ques: To display which letters are in the first string not in the second string
# I/P:
# hello
# llo
#
# O/P: he


name1 = "Selvi Jayaraman"
name2 = "vira "

res = ""

for i in name1:
    if i not in name2:
        res = res+i

print(res)
