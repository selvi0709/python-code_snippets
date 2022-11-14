# Ques: To find the sum of square of even numbers in the given list without using built-in functions

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = 0
count = 0

for i in l:
    count += 1

while count > 0:
    count = count - 1
    if (l[count] % 2) == 0:
        res += (l[count] ** 2)

print(res)
