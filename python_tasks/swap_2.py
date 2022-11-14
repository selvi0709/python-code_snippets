# Ques: To swap two numbers without using builtin

num1 = 10
num2 = 20

print("Before swapping: ",num1, num2)

temp = num1
num1 = num2
num2 = temp

print("After swapping-1: ", num1, num2)

num1, num2 = num2, num1
print("After swapping-2: ", num1, num2)
