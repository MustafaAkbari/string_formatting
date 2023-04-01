"""
In the given Python code, the numbers 2, 4, and 4 are used as format specifiers for string formatting.
Specifically, they are used to specify the width of the fields in the output string.
"""
# .format() string formatting , right align
for i in range(1, 11):
    print("No: {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print("-------------------------------")

# f-string formatting, left align
for i in range(1, 11):
    print(f"No: {i:<2} squared is {i ** 2:<4} and cubed is {i ** 3:<4}")
print("-------------------------------")
# f-string formatting, center align
for i in range(1, 11):
    print(f"No: {i:^2} squared is {i ** 2:^4} and cubed is {i ** 3:^4}")

# when we want a number of digits after decimal point we can use from .<number of digit after decimal>f
pi = 22 / 7
print(pi)
print(f"{pi:.3f}")
print(f"{pi:30.3f}")
print(f"{pi:14.5f}")
print(f"{pi:10.10f}")