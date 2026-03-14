"""Lists
i. Write a Python program to swap the minimal and maximal elements of a
given list of unique numbers.
ii. Write a Python program to implement binary search on a given list.
iii. Write a Python program to implement matrix multiplication.
iv. Given two positive integers m and n, m lines of n elements, giving an m x
n matrix A, followed by an integer c, multiply every entry of the matrix by
c and print the result.
v. Given two positive integers m and n, m lines of n elements, giving an m x
n matrix A, find the maximum element along with its index position (i.e.,
row number and column number)."""

num = [7,8,9,0,1,3]
print(num)
max=min = num[0]

m1,m2 = 0,0
print("Swapping numbers")
for i in range(len(num)):
    if num[i]>max:
        max =num[i]
        m1 =i
    if num[i]<min:
        min = num[i]
        m2 = i
print("Swapping maxima and minima values")
num[m1],num[m2] = num[m2],num[m1]
print(num)