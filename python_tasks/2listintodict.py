# Ques: To map two list into a dictionary without using builtin

list1 = [1, 2, 3, 4, 5]
list2 = ["cat", "dog", "rat", "cow", "pig"]

res = {}
count = 0

for i in list1:
    count += 1

start = 0
while start < count:
    # using builtin update()
    # res.update({list1[i]: list2[i]})

    # without using builtin
    res[list1[start]] = list2[start]
    start = start + 1

print(res)
