# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be
# printed in a comma-separated sequence on a single line.

for i in range(2000, 3201):
    if not i % 7 and i % 5:
        print(i, end=",")

print("\b")

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num = int(input("Enter number for factorial operation: "))

result = 1
count = num
while count:
    result *= count
    count -= 1

print(result)

# Version using for loop
num = int(input("Enter number for factorial operation: "))

result = 1
for i in range(1, num + 1):
    result *= i

print(result)

# Lambda version recursive approach
n = int(input("Enter number for factorial operation: "))
def short_fact(x): return 1 if x <= 1 else x*short_fact(x-1)


print(short_fact(n))

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should
# print the dictionary.Suppose the following input is supplied to the program: 8
#
# Then, the output should be:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

num = int(input("Enter number for dictionary range: "))

result = {}

for i in range(1, num + 1):
    result[i] = i * i

print(result)


